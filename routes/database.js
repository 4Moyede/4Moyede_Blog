const mongoose = require('mongoose');

mongoose.Promise = global.Promise;

// CONNECT TO MONGODB SERVER
mongoose.connect('mongodb://172.20.0.2/blog', { 
  useNewUrlParser: true,
  useUnifiedTopology: true
 })
  .then(() => console.log('Successfully connected to mongodb'))
  .catch(e => console.error(e));

var schema = mongoose.Schema;
var projectSchema = new schema({
    url: String,
    pic: String,
    header: String,
    contents: String,
    skills: String
});

module.exports = mongoose.model('projects', projectSchema);