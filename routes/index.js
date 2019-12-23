var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('socket', { title: 'Dashboard', lift_name: 'Lift BG300 Test Dashboard' });
});
router.get('/old', function(req, res, next) {
  res.render('index', { title: 'Dashboard', lift_name: 'Lift BG300 Test Dashboard' });
});
router.get('/pub', function(req, res, next) {
  res.render('index_pub', { title: 'Dashboard', lift_name: 'Lift BG300 Test Dashboard' });
});

module.exports = router;
