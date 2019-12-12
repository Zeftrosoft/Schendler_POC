topic_publish = {
  'initialStatus': '/init/lift',
  'testStatus' : '/test/status',
  'doorStatus' : '/door/status',
  'liftStatus' : '/lift/status',
  'sensor1Status' : '/sensor1/status',
  'sensor2Status' : '/sensor2/status'
} 
topic_subscribe = {
  'test' : '/test',
  'set_timer' : '/timer',
  'init_status': '/lift/status/init'
}
msg_rec = {
  '_testStart': 'start_test',
  '_testStop': 'stop_test',
  '_alive': 'alive'
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
  '_liftAscending': 'lift_ascended',
  '_liftAscended': 'lift_ascended',
  '_liftDescending': 'lift_descending',
  '_liftDecended': 'lift_descended',
  '_startedRecording': 'started_recording',
  '_recording': 'recording',
  '_stoppedRecording': 'stopped_recording',
}


    


def start_test():
  client1.publish(topic_publish['testStatus'],msg_pub['_testStarting'])
  time.sleep(5)
  client1.publish(topic_publish['testStatus'],msg_pub['_testStarted'])
  sart_set1()
  sart_set2()

def sart_set1():
  start_lift(True)

def sart_set2():
  start_lift(False)
  

def start_lift(willAscend):
  if willAscend:
    client1.publish(topic_publish['testStatus'],msg_pub['_set1Started'])
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorClosing'])
    time.sleep(3)
    
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorClosed'])
    time.sleep(1)
    client1.publish(topic_publish['liftStatus'],msg_pub['_liftAscending'])
    time.sleep(10)
    client1.publish(topic_publish['liftStatus'],msg_pub['_liftAscended'])
    time.sleep(1)
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorOpening'])
    time.sleep(3)
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorOpened'])
    client1.publish(topic_publish['testStatus'],msg_pub['_set1Completed'])

  else:
    client1.publish(topic_publish['testStatus'],msg_pub['_set2Started'])
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorClosing'])
    time.sleep(3)
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorClosed'])
    time.sleep(1)
    client1.publish(topic_publish['liftStatus'],msg_pub['_liftDescending'])
    time.sleep(10)
    client1.publish(topic_publish['liftStatus'],msg_pub['_liftDecended'])
    time.sleep(1)
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorOpening'])
    time.sleep(3)
    client1.publish(topic_publish['doorStatus'],msg_pub['_doorOpened'])
    client1.publish(topic_publish['testStatus'],msg_pub['_set2Completed'])

'''
def start_recording():
  client1.publish(topic_publish['testStatus'],msg_pub['_set1Started'])
'''
startTest = 0
startingTest = 0
testStarted = 0
stopTest = 0
initialize = 0


def handleTest(payload):
  global startTest
  if payload == msg_rec['_testStart']:
    print('Going to start Test')
    startTest = 1
    print('Ok Did it '+startTest)
  elif payload == msg_rec['_testStop']:
    client1.publish(topic_publish['initialStatus'],msg_pub['_initializing'])
    initialize()
    #stop_test()
    
def initialize():
  # Sensors And Doors And List initialized Here
  time.sleep(5)

import paho.mqtt.client as paho
import time
broker="52.8.236.185"
port=9001
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    msg.payload=msg.payload.decode("utf-8") 
    if msg.topic == topic_subscribe['init_status']:
      if msg.payload == msg_rec['_alive']:
        ret= client1.publish(topic_publish['initialStatus'],msg_pub['_yesAlive'])  
        print(ret)
    elif msg.topic == topic_subscribe['test']:
      handleTest(msg.payload)

client1= paho.Client("control1", transport='websockets') #
client1.on_publish = on_publish                         
client1.connect(broker,port)    
client1.on_subscribe = on_subscribe         
client1.on_message = on_message 

client1.subscribe(topic_subscribe['test'])
client1.subscribe(topic_subscribe['set_timer'])
client1.subscribe(topic_subscribe['init_status'])
client1.loop_start()
while True: 
  if startTest == 1:
    client1.publish(topic_publish['testStatus'],msg_pub['_testStarting'])
    client1.publish(topic_publish['initialStatus'],msg_pub['_initializing'])
    startTest = 2
  elif startTest == 2:
    initialize()
    startTest = 0
    testStarted = 1
  elif testStarted == 1:
    client1.publish(topic_publish['testStatus'],msg_pub['_testStarted'])
    testStarted = 0
  print('repeating '+str(startTest))
  time.sleep(3)



