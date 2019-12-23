var socket = require('socket.io-client')('http://localhost:3000');
socket.on('connect', function(){
  console.log('Connected To Server');
  socket.emit('join', {channel: 'lift_status', id: 'NodeClient'})
});
socket.on('message_python', (data) => {
  console.log('Got Python Message');
  console.log(data);
  
});
socket.on('disconnect', function(){
  console.log('Disconnected From Server');
  
});