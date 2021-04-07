const fs = require('fs');
const { google } = require('googleapis');


class googleAPI {
  constructor() {
    this.FILEPATH = './public/images/projects/';
    this.KEYFILE = './key/service_account.json';
    this.SCOPES = ['https://www.googleapis.com/auth/drive'];

    this.auth = new google.auth.GoogleAuth({
      keyFile: this.KEYFILE,
      scopes: this.SCOPES,
    });

    this.drive = google.drive({
      version: 'v3',
      auth: this.auth
    });
  }

  download() {
    return new Promise((resolve, reject) => {
      this.drive.files.list({
        pageSize: 10,
        fields: 'nextPageToken, files(id, name, size)',
      }, (err, res) => {
        if (err) {
          console.log('The API returned an error: ' + err);
          reject();
        } else {
          const files = res.data.files;
          if (files.length) {
            files.map((file) => {
              let path = this.FILEPATH + file.name;
              this.drive.files
                .get({ fileId: file.id, alt: 'media' }, { responseType: 'stream' })
                .then(res => {
                  const dest = fs.createWriteStream(path);

                  res.data
                    .on('error', err => {
                      console.log(`GET /google/drive/${file.name} \x1b[31m404\x1b[0m`)
                      reject();
                    })
                    .on('end', () => {
                      console.log(`GET /google/drive/${file.name} \x1b[32m200\x1b[0m`);
                      resolve();
                    })
                    .pipe(dest);
                });
            });
          }
        }
      });
    });
  }
}

module.exports = new googleAPI();