topic_publish = {
  'initialStatus': '/init/lift',
  'testStatus' : '/test/status',
  'doorStatus' : '/door/status',
  'liftStatus' : '/lift/status',
  'sensor1Status' : '/sensor1/status',
  'sensor2Status' : '/sensor2/status',
  'sensorAction' : '/sensor/action'
} 
topic_subscribe = {
  'test' : '/test',
  'set_timer' : '/timer',
  'init_status': '/lift/status/init',
  'sensorAck' : '/sensor/ack'
}
msg_rec = {
  '_testStart': 'start_test',
  '_testStop': 'stop_test',
  '_alive': 'alive',
  '_sensorsInitialized': 'sensors_initialized'
}
msg_pub = {
  '_yesAlive': 'yes_alive',
  '_initializing': 'initializing',
  '_testStarting': 'starting_test',
  '_testStopping': 'stopping_test',
  '_testStarted': 'test_started',
  '_testCompleted': 'test_completed',
  '_testStopped': 'test_stopped',
  '_set1Started': 'set1_started',
  '_set1Completed': 'set1_completed',
  '_set2Started': 'set2_started',
  '_set2Completed': 'set2_completed',
  '_dataSaved': 'data_saved',
  '_doorOpening': 'door_opening',
  '_doorOpened': 'door_opened',
  '_doorClosing': 'door_closing',
  '_doorClosed': 'door_closed',
  '_liftAscending': 'lift_ascending',
  '_liftAscended': 'lift_ascended',
  '_liftDescending': 'lift_descending',
  '_liftDecended': 'lift_descended',
  '_startedRecording': 'started_recording',
  '_recording': 'recording',
  '_stoppedRecording': 'stopped_recording',

  '_startRecording': 'start_recording',
  '_stopRecording': 'stop_recording',
  '_saveData': 'save_data'
  
}


def start_recording():
  client1.publish(topic_publish['sensorAck'],msg_pub['_startRecording'])

def start_recording():
  client1.publish(topic_publish['sensorAck'],msg_pub['_stopRecording'])

import paho.mqtt.client as paho
import time
broker="52.8.236.185"
port=1883

startTestInitiated = False
liftInitialized = False
sensorsInitialized = False
publisherClientId = "temp_sender_client_Controller"
subscriberClientId = "Temp_Subscriber_client_controller"
def createNewClientAndPublish(what_topic, what_msg):
  print(what_topic, what_msg)
  client2= paho.Client(publisherClientId) #                  , transport='websockets'
  client2.connect(broker,port)    
  client2.publish(what_topic, what_msg)
  client2.disconnect()

def handleTest(payload):
  global startTestInitiated
  if payload == msg_rec['_testStart']:
    startTestInitiated = True
    initialize()

    
  elif payload == msg_rec['_testStop']:
    initialize()
    #stop_test()

def initialize():
  global liftInitialized
  createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_initializing'])
  time.sleep(5)
  liftInitialized = True

def start_test():
  global startTestInitiated
  global liftInitialized
  global sensorsInitialized
  time.sleep(5)
  createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_testStarted'])
  sart_set1()
  time.sleep(10)
  sart_set2()
  createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_testCompleted'])
  createNewClientAndPublish(topic_publish['sensorAction'],msg_pub['_saveData'])
  startTestInitiated = False
  liftInitialized = False
  sensorsInitialized = False

def sart_set1():
  start_lift(True)

def sart_set2():
  start_lift(False)
  

def start_lift(willAscend):
  if willAscend:
    createNewClientAndPublish(topic_publish['sensorAction'],msg_pub['_startRecording'])
    createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_set1Started'])
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorClosing'])
    time.sleep(3)
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorClosed'])
    time.sleep(1)
    createNewClientAndPublish(topic_publish['liftStatus'],msg_pub['_liftAscending'])
    time.sleep(10)
    createNewClientAndPublish(topic_publish['liftStatus'],msg_pub['_liftAscended'])
    time.sleep(1)
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorOpening'])
    time.sleep(3)
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorOpened'])
    createNewClientAndPublish(topic_publish['sensorAction'],msg_pub['_stopRecording'])
    createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_set1Completed'])

  else:
    createNewClientAndPublish(topic_publish['sensorAction'],msg_pub['_startRecording'])
    createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_set2Started'])
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorClosing'])
    time.sleep(3)
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorClosed'])
    time.sleep(1)
    createNewClientAndPublish(topic_publish['liftStatus'],msg_pub['_liftDescending'])
    time.sleep(10)
    createNewClientAndPublish(topic_publish['liftStatus'],msg_pub['_liftDecended'])
    time.sleep(1)
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorOpening'])
    time.sleep(3)
    createNewClientAndPublish(topic_publish['doorStatus'],msg_pub['_doorOpened'])
    createNewClientAndPublish(topic_publish['sensorAction'],msg_pub['_stopRecording'])
    createNewClientAndPublish(topic_publish['testStatus'],msg_pub['_set2Completed'])
    
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(mqttc, obj, msg):
    global sensorsInitialized
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    msg.payload=msg.payload.decode("utf-8") 
    if msg.topic == topic_subscribe['init_status']:
      if msg.payload == msg_rec['_alive']:
        client1.publish(topic_publish['initialStatus'],msg_pub['_yesAlive'])  
    elif msg.topic == topic_subscribe['test']:
      handleTest(msg.payload)
    elif msg.topic == topic_subscribe['sensorAck']:
      print('Sensor Initialized Is True')
      print(msg.payload, msg_rec['_sensorsInitialized'])
      if msg.payload == msg_rec['_sensorsInitialized']:
        print('Sensor Initialized')
        sensorsInitialized = True


client1= paho.Client(subscriberClientId) #, transport='websockets'                  
client1.connect(broker,port)    
client1.on_subscribe = on_subscribe         
client1.on_message = on_message 

client1.subscribe(topic_subscribe['test'])
client1.subscribe(topic_subscribe['set_timer'])
client1.subscribe(topic_subscribe['init_status'])
client1.subscribe(topic_subscribe['sensorAck'])
client1.loop_start()
while(True):
  if startTestInitiated:
    if liftInitialized and sensorsInitialized:
      start_test()



