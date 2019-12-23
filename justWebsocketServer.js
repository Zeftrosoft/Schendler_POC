const express = require('express'); // using express 
const socketIO = require('socket.io'); 
const http = require('http')  
const port = process.env.PORT||3000 // setting the port  
let app = express(); 
let server = http.createServer(app) 
let io = socketIO(server) 
server.listen(port); 


// var gaze = io.of('/1234').on('connection', function (socket) {
//   console.log('Connected To 1234 Namespace');
  
//   socket.on('message', function (gdata) {
//     console.log('Got Data In 1234 Namespace');
//     console.log(gdata);
//     gaze.emit('message_from', gdata.channel)
//   })
//   socket.on('broadcast message', function (data) {
//     console.log(data);
//     socket.to(data.channel).emit('send_message',data.message)
//   });
// })

io.on('connection', (socket)=>{
  console.log('New user connected');
  // socket connection indicates what mqtt topic to subscribe to in data.topic
  socket.on('join', function (data) {
    id = data['id']
    channel = data['channel']
    socket.join(channel);
    console.log('User '+id+' Has Entered the room '+channel);
  });
  socket.on('start_test', function (data) {
    // id = data['id']
    // channel = data['channel']
    // socket.join(channel);
    console.log('Start Test');
    console.log(data);
    socket.emit('message_from', data.message)
    socket.broadcast.emit('start_test', data.message)
  });
  socket.on('sleep', function (data) {
    // id = data['id']
    // channel = data['channel']
    // socket.join(channel);
    socket.broadcast.emit('message_python', data.message)
    console.log('Got Sleep Message');
    console.log(data);
    //socket.emit('message_from', data.message)
  });
  socket.on('stop_all', function (data) {
    // id = data['id']
    // channel = data['channel']
    // socket.join(channel);
    socket.broadcast.emit('stop_all', data.message)
    console.log('Got Stop Test');
    console.log(data);
    //socket.emit('message_from', data.message)
  });
  socket.on('message', function (data) {
    // id = data['id']
    // channel = data['channel']
    // socket.join(channel);
    console.log('Got Message');
    console.log(data);
    //socket.emit('message_from', data.message)
  });
  
   // when socket connection publishes a message, forward that message
    // the the mqtt broker
  // socket.on('broadcast message', function (data) {
  //   console.log(data);
  //   socket.to(data.channel).emit('send_message',data.message)
    
  // });
  // when server disconnects from user 
  socket.on('disconnect', ()=>{ 
    console.log('disconnected from user'); 
  }); 
});