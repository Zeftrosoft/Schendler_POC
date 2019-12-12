var mqtt    = require('mqtt');
const express = require('express'); // using express 
const socketIO = require('socket.io'); 
const http = require('http')  
const port = process.env.PORT||3000 // setting the port  
let app = express(); 
let server = http.createServer(app) 
let io = socketIO(server) 
server.listen(port); 
var mqtt_host = 'mqtt://52.8.236.185'
var mqtt_client  = mqtt.connect(mqtt_host,{clientId:"mqttjs01azizahtasnodejsclient"});
// make a connection with the user from server side
io.on('connection', (socket)=>{
  // socket connection indicates what mqtt topic to subscribe to in data.topic
  console.log('New user connected');
  socket.on('subscribe', function (data) {
    console.log('Subscribing to '+data.topic);
    socket.join(data.topic);
    mqtt_client.subscribe(data.topic);
  });
   // when socket connection publishes a message, forward that message
    // the the mqtt broker
  socket.on('publish', function (data) {
    console.log('Publishing to '+data.topic);
    mqtt_client.publish(data.topic,data.payload);
  });
  // when server disconnects from user 
  socket.on('disconnect', ()=>{ 
    console.log('disconnected from user'); 
  }); 
});
// listen to messages coming from the mqtt broker
mqtt_client.on('message', function (topic, payload, packet) {
  console.log(topic+'='+payload);
  io.sockets.emit('mqtt',{'topic':String(topic),
                          'payload':String(payload)});
});

mqtt_client.on("connect",function(){	
  console.log("Connected to Mqtt Port 1883: Host "+mqtt_host);
})

mqtt_client.on("error",function(error){ 
  console.log("Can't connect"+error);
});