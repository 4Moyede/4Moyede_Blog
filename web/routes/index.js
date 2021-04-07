const express = require('express');
const fetch = require('node-fetch');
const async = require('async');
const googleAPI = require('./drive');

let router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  googleAPI.download();
  fetch("http://172.20.0.2:8000/api/data")
    .then(data => {
      data.json()
        .then(contents => {
          res.render('index.ejs', contents);
        });
    });

});

module.exports = router;