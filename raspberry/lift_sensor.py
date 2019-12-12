topic_publish = {
  # 'initialStatus': '/init/lift',
  'testStatus' : '/test/status',
  # 'doorStatus' : '/door/status',
  # 'liftStatus' : '/lift/status',
  'sensor1Status' : '/sensor1/status',
  'sensor2Status' : '/sensor2/status',
  'sensorAck' : '/sensor/ack'
} 
topic_subscribe = {
  # 'test' : '/test',
  # 'set_timer' : '/timer',
  # 'init_status': '/lift/status/init',
  'sensorAction' : '/sensor/action',
  'testStatus' : '/test/status'
}
msg_pub = {
  '_initializingSensors': 'sensor_initializing',
  '_initializedSensors': 'sensor_initialized',
  '_sensorsInitialized': 'sensors_initialized',
  '_startedRecording': 'started_recording',
  '_recording': 'recording',
  '_stoppedRecording': 'stopped_recording',
  '_dataSaved': 'data_saved',
}
msg_rec = {
  # '_yesAlive': 'yes_alive',
  # '_testStarting': 'starting_test',
  # '_testStopping': 'stopping_test',
  # '_testStarted': 'test_started',
  # '_testCompleted': 'test_completed',
  # '_testStopped': 'test_stopped',
  # '_set1Started': 'set1_started',
  # '_set1Completed': 'set1_completed',
  # '_set2Started': 'set2_started',
  # '_set2Completed': 'set2_completed',
  # '_dataSaved': 'data_saved',
  # '_doorOpening': 'door_opening',
  # '_doorOpened': 'door_opened',
  # '_doorClosing': 'door_closing',
  # '_doorClosed': 'door_closed',
  # '_liftAscending': 'lift_ascending',
  # '_liftAscended': 'lift_ascended',
  # '_liftDescending': 'lift_descending',
  # '_liftDecended': 'lift_descended',
  '_initializing': 'initializing',
  '_startRecording': 'start_recording',
  '_stopRecording': 'stop_recording',
  '_saveData': 'save_data'
}

import paho.mqtt.client as paho
import time
broker="52.8.236.185"
port=9001

shouldStartRecord = False
shouldStopRecord = False
publisherClientId = "temp_sender_client_12123213ZeusSensor"
subscriberClientId = "Sensor_Client_21123123123123"
def createNewClientAndPublish(what_topic, what_msg):
  print(what_topic, what_msg)
  client2= paho.Client(publisherClientId, transport='websockets')               
  client2.connect(broker,port)    
  client2.publish(what_topic, what_msg)
  client2.disconnect()

def start_recording():
  createNewClientAndPublish(topic_publish['sensor1Status'],msg_pub['_startedRecording'])
  print('Recording Started For Sensor 1....')
  createNewClientAndPublish(topic_publish['sensor1Status'],msg_pub['_recording'])

  createNewClientAndPublish(topic_publish['sensor2Status'],msg_pub['_startedRecording'])
  print('Recording Started For Sensor 2....')
  createNewClientAndPublish(topic_publish['sensor2Status'],msg_pub['_recording'])

def stop_recording():
  createNewClientAndPublish(topic_publish['sensor1Status'],msg_pub['_stoppedRecording'])
  print('Recording Stopped For Sensor 1....')

  createNewClientAndPublish(topic_publish['sensor2Status'],msg_pub['_stoppedRecording'])
  print('Recording Stopped For Sensor 2....')

def handleAction(payload):
  global shouldStartRecord
  global shouldStopRecord
  if payload == msg_rec['_startRecording']:
    shouldStartRecord = True
  if payload == msg_rec['_stopRecording']:
    shouldStopRecord = True
  if payload == msg_rec['_saveData']:
    save_data()

def handleTest(payload):
  print('handle test Called...')
  print(payload)
  if payload == msg_rec['_initializing']:
    initialize()
    
  

def initialize():
  print('Initializing Sensors...')
  createNewClientAndPublish(topic_publish['sensor1Status'],msg_pub['_initializingSensors'])
  createNewClientAndPublish(topic_publish['sensor2Status'],msg_pub['_initializingSensors'])
  time.sleep(5)
  createNewClientAndPublish(topic_publish['sensor1Status'],msg_pub['_initializedSensors'])
  createNewClientAndPublish(topic_publish['sensor2Status'],msg_pub['_initializedSensors'])
  createNewClientAndPublish(topic_publish['sensorAck'],msg_pub['_sensorsInitialized'])

def save_data():
  print('Saving Data...')
  time.sleep(4)
  createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_dataSaved'])

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    msg.payload=msg.payload.decode("utf-8") 
    if msg.topic == topic_subscribe['testStatus']:
      handleTest(msg.payload)
    elif msg.topic == topic_subscribe['sensorAction']:
      handleAction(msg.payload)

client1= paho.Client(subscriberClientId, transport='websockets')                  
client1.connect(broker,port)    
client1.on_subscribe = on_subscribe         
client1.on_message = on_message 

client1.subscribe(topic_subscribe['testStatus'])
client1.subscribe(topic_subscribe['sensorAction'])
# client1.subscribe(topic_subscribe['init_status'])
client1.loop_start()
while(True):
  if shouldStartRecord:
    start_recording()
    shouldStartRecord = False
  elif shouldStopRecord:
    stop_recording()
    shouldStopRecord = False

