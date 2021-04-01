const express = require('express');
const projects = require('./database.js');

var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  projects.find( { }, (err, projects) => {
    var result = {};
    result.project = projects;
    result.size = result.project.length;
    
    res.render('index.ejs', result);
  });
});

module.exports = router;