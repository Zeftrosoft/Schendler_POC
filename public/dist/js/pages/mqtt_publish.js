var host = mqtt_host;
var port = mqtt_port;
var publish_client = 'azizahtas_publish13asdkjbzxkchgigd738'

var _topicToPublish = ''
var _messageToSend = ''
// var client_publish;
function sendMessage() {
  console.log("Connecting to " + host + " " + port + 'With Publish Client: '+publish_client);
  client_publish = new Paho.MQTT.Client(host, port, publish_client);
  var options = {
    timeout: 30000,
    keepAliveInterval: 10,
    onSuccess: onConnect,
    onFailure: onFail
  };
  client_publish.onConnectionLost = onConnectionLost;
  client_publish.connect(options);
}

function onConnect() {
  console.log('Sending message: '+_messageToSend+' : '+_topicToPublish);
  
  var publish_message = new Paho.MQTT.Message(_messageToSend);
  publish_message.destinationName = _topicToPublish
  client_publish.send(publish_message)
}
function onFail() {
  console.log("Failed To Connect By publish Client");
  
}
function onConnectionLost() {
  console.log('Publisher Connection Lost');
}

function isAlive() {
  _topicToPublish = topic_publish.init_status
  _messageToSend = msg_pub._alive
  sendMessage()
}

function start_test() {
  _messageToSend = msg_pub._testStart
  _topicToPublish = topic_publish.test
  sendMessage()
}

// window.setInterval(function(){
//   isAlive()
// }, 120000);