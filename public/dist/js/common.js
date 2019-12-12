var local = 'http://localhost:3000'
var online = 'https://laptopsoft.herokuapp.com'
var mqtt_host = "52.8.236.185"
var mqtt_port = 9001
var used_host = online

var topic_publish = {
  test : '/test',
  set_timer : '/timer',
  init_status: '/lift/status/init'
}

var topic_subscribe = {
  initialStatus: '/init/lift', // connected, disconnected
  testStatus : '/test/status',
  doorStatus : '/door/status',
  liftStatus : '/lift/status',
  sensor1Status : '/sensor1/status',
  sensor2Status : '/sensor2/status'
} 

var msg_pub = {
  _testStart: 'start_test',
  _testStop: 'stop_test',
  _alive: 'alive'
}

var msg_rec = {
  _yesAlive: 'yes_alive',
  _initializing: 'initializing',

  _testStarting: 'starting_test',
  _testStopping: 'stopping_test',
  _testStarted: 'test_started',
  _testCompleted: 'test_completed',
  _testStopped: 'test_stopped',
  _set1Started: 'set1_started',
  _set1Completed: 'set1_completed',
  _set2Started: 'set2_started',
  _set2Completed: 'set2_completed',
  _dataSaved: 'data_saved',

  _doorOpening: 'door_opening',
  _doorOpened: 'door_opened',
  _doorClosing: 'door_closing',
  _doorClosed: 'door_closed',

  _liftAscending: 'lift_ascending',
  _liftAscended: 'lift_ascended',
  _liftDescending: 'lift_descending',
  _liftDecended: 'lift_descended',

  _initializingSensors: 'sensor_initializing',
  _initializedSensors: 'sensor_initialized',
  _startedRecording: 'started_recording',
  _recording: 'recording',
  _stoppedRecording: 'stopped_recording',
}

const Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  showConfirmButton: false,
  timer: 3000
});

function notifyUser(type, message) {
  Toast.fire({
    type: type,
    title: message
  })
}