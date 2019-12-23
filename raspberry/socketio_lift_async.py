import socketio
import asyncio
import time
sio = socketio.AsyncClient()
namespace = '/1234'
loop = asyncio.get_event_loop()
def my_background_task(my_argument):
    print('I Have been started: '+my_argument)
    time.sleep(10)
    print('I Have been completed: '+my_argument)


@sio.event()
async def connect():
    print('connection established')
    await sio.emit('join', {'channel': 'lift_status', 'id': 'PythonClient'}, )
    # sio.emit('gaze', {'message': 'Gaze', 'id': 'PythonClient'})
    # sio.start_background_task(my_background_task, 'On Connect')

@sio.event()
async def message_python(data):
    print(data)
    
    await sio.start_background_task(my_background_task, 'On Message')
    print('Called Background Task')
    #sio.emit('broadcast message', {'response': 'my response'}, room='test')

@sio.event()
async def disconnect():
    print('disconnected from server')


async def start_server():
  await sio.connect('http://localhost:3000')
  await sio.wait()
  #while True:
    #pass

if __name__ == '__main__':
    loop.run_until_complete(start_server())



