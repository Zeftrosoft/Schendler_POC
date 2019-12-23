import socketio
import asyncio
import time
sio = socketio.Client()
namespace = '/1234'

def my_background_task(my_argument):
    print('I Have been started: '+my_argument)
    #time.sleep(10)
    a = 0
    while a <= 10:
      print('3 Second Sleep')
      sio.emit('sleep', {'message': 'Count: '+str(a)})
      time.sleep(3)
      a=a+1
    print('I Have been completed: '+my_argument)


@sio.event()
def connect():
    print('connection established')
    sio.emit('join', {'channel': 'lift_status', 'id': 'PythonClient'})
    # sio.emit('gaze', {'message': 'Gaze', 'id': 'PythonClient'})
    # sio.start_background_task(my_background_task, 'On Connect')

@sio.event()
def message_python(data):
    print(data)
    
    sio.start_background_task(my_background_task, 'On Message')
    print('Called Background Task')
    #sio.emit('broadcast message', {'response': 'my response'}, room='test')

@sio.event()
def stop_all(data):
    print(data)
    print('Stopping All Tests')
    #sio.emit('broadcast message', {'response': 'my response'}, room='test')

@sio.event()
def disconnect():
    print('disconnected from server')


def start_server():
  sio.connect('http://localhost:3000')
  #sio.wait()
  while True:
    pass

start_server()




