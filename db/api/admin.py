from django.contrib import admin
from api.models import Introduce, Projects, TechStack

from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaIoBaseDownload

from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient

from os import path
from io import BytesIO
from json import loads
from PIL import Image

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
APIKEY_FILE = path.join(path.join(BASE_DIR, 'key'), 'service_account.json')
SSHKEY_FILE = path.join(path.join(BASE_DIR, 'key'), 'ssh_key.json')
FILE_DIR = path.join(BASE_DIR, 'download')

SCOPE = ['https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(APIKEY_FILE, scopes=SCOPE)
service = build(serviceName='drive', version='v3', credentials=credentials)

def DownloadThumbnail(modeladmin, request, queryset):
    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found. Check Google Drive')
        for query in queryset:
            query.thumbnail = "loading.png"
    else:
        found = False
        for query in queryset:
            for item in items:
                if query.thumbnail == item['name']:
                    FILE_PATH = path.join(FILE_DIR, item['name'])
                    download(item['id'], FILE_PATH)
                    transfer(FILE_PATH)
                    found = True
                    break
            if not found:
                query.thumbnail = "loading.png"
DownloadThumbnail.short_description = "Download Thumbnail file from google drive"

def download(fid, path):
    request = service.files().get_media(fileId=fid)
    fh = BytesIO()
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("%s Download %d%%." % (path ,int(status.progress() * 100)))

    img = Image.open((fh))
    img.save(path)
    
def transfer(path):
    auth = loads(open(SSHKEY_FILE).read())

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect("172.20.0.3", username=auth['username'], password=auth['password'])

    # SCPCLient takes a paramiko transport as an argument
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(path, remote_path="/app/server/public/images/projects/")


# Register your models here.
class IntroduceAdmin(admin.ModelAdmin):
    pass

class ProjectsAdmin(admin.ModelAdmin):
    actions = [ DownloadThumbnail ]

class TechStackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Introduce, IntroduceAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(TechStack, TechStackAdmin)
