import socketio
#import eventlet
import time
sio = socketio.Client()
namespace = '/1234'

# our gloabal worker
workerObject = None

class Worker(object):

    switch = False
    unit_of_work = 0

    def __init__(self, socketio):
        """
        assign socketio object to emit
        """
        self.socketio = socketio
        self.switch = True

    def do_work(self):
        """
        do work and emit message
        """

        while self.switch:
            self.unit_of_work += 1

            # must call emit from the socket io
            # must specify the namespace
            # self.socketio.emit("update", {"msg": self.unit_of_work}, namespace="/work")
            self.socketio.emit('sleep', {'message': 'Count: '+str(self.unit_of_work)})
            # important to use eventlet's sleep method
            self.socketio.sleep(1)

    def stop(self):
        """
        stop the loop
        """
        self.switch = False

    def start(self):
        """
        start the loop
        """
        self.unit_of_work = 0
        self.switch = True

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
    global worker
    print('connection established')
    sio.emit('join', {'channel': 'lift_status', 'id': 'PythonClient'})
    worker = Worker(sio)
    # sio.emit('gaze', {'message': 'Gaze', 'id': 'PythonClient'})
    # sio.start_background_task(my_background_task, 'On Connect')

@sio.event()
def message_python(data):
    print(data)
    
    sio.start_background_task(target=worker.do_work)
    print('Called Background Task')
    #sio.emit('broadcast message', {'response': 'my response'}, room='test')

@sio.event()
def start_test(data):
    print(data)
    print('Starting Test')
    worker.start()
    sio.start_background_task(target=worker.do_work)
    

@sio.event()
def stop_all(data):
    print(data)
    print('Stopping All Tests')
    worker.stop()
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