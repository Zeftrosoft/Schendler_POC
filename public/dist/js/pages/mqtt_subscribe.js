
var reconnecttime = 2000;
var host = mqtt_host;
var port = mqtt_port;
var subscribe_client = 'sdaighadia231232kjhcfkjhzfdlkln'
// var client_subscribe;
// This Is Mqtt Subscribe File 
// function MqttConnect() {
  console.log("Connecting to " + host + " " + port + 'With Subscribe Client: '+subscribe_client);
client_subscribe = new Paho.MQTT.Client(host, port, subscribe_client);
var options = {
  timeout: 30000,
  keepAliveInterval: 10,
  onSuccess: onConnect,
  onFailure: onFail
};
client_subscribe.onMessageArrived = onMessageArrived;
client_subscribe.onConnectionLost = onSubConnectionLost;
client_subscribe.connect(options);
// }


var serverOnlineId = "#serverOnline"
var liftOnlineId = "#liftOnline"

function onConnect() {
  console.log("Connected Successfully");
  if($(serverOnlineId).hasClass('btn-danger')){
    $(serverOnlineId).removeClass('btn-danger')
    $(serverOnlineId).addClass('btn-success')
  } else $(serverOnlineId).addClass('btn-success')
 
  //msgtosend= new Paho.MQTT.Message("Start_Test"); 
  //msgtosend.destinationName="house/bulb";
  //mqtt.send(msgtosend);
  client_subscribe.subscribe(topic_subscribe.initialStatus)
  client_subscribe.subscribe(topic_subscribe.testStatus)
  client_subscribe.subscribe(topic_subscribe.doorStatus)
  client_subscribe.subscribe(topic_subscribe.liftStatus)
  client_subscribe.subscribe(topic_subscribe.sensor1Status)
  client_subscribe.subscribe(topic_subscribe.sensor2Status)
}
function onFail() {
  console.log("Failed To Connect");
  if($(serverOnlineId).hasClass('btn-success')){
    $(serverOnlineId).removeClass('btn-success')
    $(serverOnlineId).addClass('btn-danger')
  } else $(serverOnlineId).addClass('btn-danger')
  
}
function onSubConnectionLost() {
  console.log('Subscriber Connection Lost');
  //MqttConnect()
}
function onMessageArrived(recieved) {
  //console.log("message recieved but not displayed")
  var topic = recieved.destinationName
  var msg = recieved.payloadString
  console.log(msg+' : '+topic);
  if(topic == topic_subscribe.initialStatus) {
    if(msg == msg_rec._yesAlive) {
      if($(liftOnlineId).hasClass('btn-danger')){
        $(liftOnlineId).removeClass('btn-danger')
        $(liftOnlineId).addClass('btn-success')
      } 
    }
    console.log(omsg);
  }
}
// MqttConnect()
// function start_test() {
//   //document.getElementById("sos1").innerHTML = "Have a nice day!";
//   //$('#sos1').html("Starting Test....")
//   //$('#sos1').css("color","red")
//   var msgtosend = new Paho.MQTT.Message("Start_Test");
//   msgtosend.destinationName = "Lift1";
//   mqtt.send(msgtosend);
//   //mqtt.subscribe("Lift1")
//   $('#sos1').css("color", "Green")

// }
// function stop_test() {
//   //document.getElementById("sos1").innerHTML = "Have a nice day!";
//   //$('#sos1').html("Starting Test....")
//   //$('#sos1').css("color","red")
//   msgtosend = new Paho.MQTT.Message("Stop_Test");
//   msgtosend.destinationName = "Lift1";
//   mqtt.send(msgtosend);
//   // mqtt.subscribe("Lift1")
//   $('#sos1').css("color", "Red")

// }

// function isAlive() {
//   var alive_message = new Paho.MQTT.Message(msg_pub._alive);
//   alive_message.destinationName = topic_publish.init_status
//   client_subscribe.send(alive_message)
// }

// window.setInterval(function(){
//   isAlive()
// }, 5000);

