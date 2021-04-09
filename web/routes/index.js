const express = require('express');
const fetch = require('node-fetch');

let router = express.Router();

/* GET home page. */
router.get('/', (req, res, next) => {
  fetch("http://172.20.0.2:8000/api/data")
    .then(data => {
      data.json()
        .then(contents => {
          res.render('index.ejs', contents);
        }
    });
});

module.exports = router;