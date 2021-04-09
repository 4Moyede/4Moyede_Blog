from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

from sys import argv
from os import path

if __name__ == "__main__":
  BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
  
  APIKEY_FILE = path.join(path.join(BASE_DIR, 'key'), 'service_account.json')
  SCOPE = ['https://www.googleapis.com/auth/drive']
  credentials = ServiceAccountCredentials.from_json_keyfile_name(APIKEY_FILE, scopes=SCOPE)
  service = build(serviceName='drive', version='v3', credentials=credentials)

  FILE_DIR = path.join(BASE_DIR, 'upload')
  
  if len(argv) < 2:
    print("[ File List ]")
    results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
      print('No files found. Check Google Drive')
    else:
      for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))

  else:
    COMMAND = argv[1]
    if COMMAND == "upload":
      FILE_NAME = argv[2]
      file_metadata = { 'name': FILE_NAME }
      media = MediaFileUpload(path.join(FILE_DIR, FILE_NAME), mimetype='image/png')
      
      upload = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
      print('%s upload success!' % upload.get('id'))

    elif COMMAND == "delete":
      FID = argv[2]

      delete = service.files().delete(fileId=FID).execute()
      print('%s deleted..' % FID)
