var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  json = require('../public/projects/projects_list.json');

  var result = { };
  result.project = json;
  result.size = result.project.length;
  
  res.render('index.ejs', result);
});

module.exports = router;