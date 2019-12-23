//var socket=io(live_websocket_host) 
// make connection with server from user side
var socket = io.connect(live_websocket_host);

var serverOnlineId = "#serverOnline"
var liftOnlineId = "#liftOnline"
var lift_online = false
var server_online = false
socket.on('gaze', function (data) {
  console.log(data);
});
socket.on('connect', function(){ 
  console.log('Connected to Socket Server') 
  server_online = true
  if($(serverOnlineId).hasClass('btn-danger')){
    $(serverOnlineId).removeClass('btn-danger')
    $(serverOnlineId).addClass('btn-success')
  } else $(serverOnlineId).addClass('btn-success')
  
  socket.on('message_from', function (msg) {
    console.log(msg)
  })
  socket.emit('join', {channel: 'lift_status', id: 'ClientJs'});
  // socket.on('mqtt', function (msg) {
  //   console.log(msg.topic+' '+msg.payload);
  //   switch (msg.topic) {
  //     case topic_subscribe.initialStatus:
  //       if(msg.payload == msg_rec._yesAlive) {
  //         lift_online = true
  //         if($(liftOnlineId).hasClass('btn-danger')){
  //           $(liftOnlineId).removeClass('btn-danger')
  //           $(liftOnlineId).addClass('btn-success')
  //         } 
  //       }
  //       break;
  //     case topic_subscribe.testStatus:
  //       switch (msg.payload) {
  //         case msg_rec._initializing:
  //           $('#testStatus').text('Initializing Test ..')
  //           $('#sensor1Status').text('Initializing...')
  //           $('#sensor2Status').text('Initializing...')
  //         break;
  //         case msg_rec._testStarting:
  //             console.log('Test Starting');
  //             $('#testStatus').text('Test Starting ..')
  //           break;
  //         case msg_rec._testStarted:
  //             console.log('Test Started');
  //             $('#initializing_sensors').text('')
  //             $('#testStatus').text('Test Started')
  //           break;
  //         case msg_rec._testStopping:
  //             $('#testStatus').text('Stopping Test..')
  //             break;
  //         case msg_rec._testStopped:
  //             $('#testStatus').text('Test Stopped')
  //             break;
  //         case msg_rec._set1Started:
  //             $('#set1Status').text('Set One Started')
  //             break;
  //         case msg_rec._set2Started:
  //             $('#set2Status').text('Set Two Started')
  //             break;
  //         case msg_rec._set1Completed:
  //             $('#set1Status').text('Set One Completed')
  //             break;
  //         case msg_rec._set2Completed:
  //             $('#set2Status').text('Set Two Completed')
  //             break;
  //         case msg_rec._dataSaved:
  //             notifyUser('success','Data Saved')
  //             $('#dataSaved').html(`
  //             <div class="callout callout-info">
  //             <h3><span style="color:rgb(41, 167, 69)">Data Saved Successfully</span></h3>
  //             </div>
  //             `)
  //            $('#dataPanel').html(`
  //            <div class="col-md-12" id="dataPanel"><br><div class="card-header"><h3 class="card-title">Simple Full Width Table</h3><div class="card-tools"><ul class="pagination pagination-sm float-right"><li class="page-item"><a class="page-link" href="#">«</a></li><li class="page-item"><a class="page-link" href="#">1</a></li><li class="page-item"><a class="page-link" href="#">2</a></li><li class="page-item"><a class="page-link" href="#">3</a></li><li class="page-item"><a class="page-link" href="#">»</a></li></ul></div><!-- /.card-header--><div class="card-body p-0"><table class="table"><thead><tr><th style="width: 10px">#</th><th style="width: 500px">Task</th><th style="width: 500px">Progress</th><th style="width: 90px">Label</th></tr></thead><tbody><tr><td>1.</td><td>Update software</td><td><div class="progress progress-xs"><div class="progress-bar progress-bar-danger" style="width: 55%"></div></div></td><td><span class="badge bg-danger">55%</span></td></tr><tr><td>2.</td><td>Clean database</td><td><div class="progress progress-xs"><div class="progress-bar bg-warning" style="width: 70%"></div></div></td><td><span class="badge bg-warning">70%</span></td></tr><tr><td>3.</td><td>Cron job running</td><td><div class="progress progress-xs progress-striped active"><div class="progress-bar bg-primary" style="width: 30%"></div></div></td><td><span class="badge bg-primary">30%</span></td></tr><tr><td>4.</td><td>Fix and squish bugs</td><td><div class="progress progress-xs progress-striped active"><div class="progress-bar bg-success" style="width: 90%"></div></div></td><td><span class="badge bg-success">90%</span></td></tr></tbody></table></div></div></div>
  //            `)
  //             break;
  //         default:
  //           break;
  //     }
  //     break;
  //     case topic_subscribe.doorStatus:
  //       switch (msg.payload) {
  //         case msg_rec._doorOpening:
  //             $('#doorStatus').text('Door Opening ...')
  //           break;
  //         case msg_rec._doorOpened:
  //             $('#doorStatus').text('Door Opened')
  //           break;
  //         case msg_rec._doorClosing:
  //             $('#doorStatus').text('Door Closing ...')
  //             break;
  //         case msg_rec._doorClosed:
  //             $('#doorStatus').text('Door Closed ...')
  //             break;

  //         default:
  //           break;
  //     } 
  //     break;   
  //     case topic_subscribe.liftStatus:
  //       switch (msg.payload) {
  //         case msg_rec._liftAscending:
  //             $('#liftStatus').text('Lift Ascending ...')
  //             break;
  //         case msg_rec._liftAscended:
  //             $('#liftStatus').text('Lift Ascended')
  //             break;
  //         case msg_rec._liftDescending:
  //             $('#liftStatus').text('Lift Descending ...')
  //             break;
  //         case msg_rec._liftDecended:
  //             $('#liftStatus').text('Lift Descended')
  //             break;
  //         default:
  //             break;
  //       } 
  //       break;  
  //       case topic_subscribe.sensor1Status:
  //         switch (msg.payload) {
  //           case msg_rec._startedRecording:
  //               $('#sensor1Status').text('Started Recording')
  //               break;
  //           case msg_rec._recording:
  //               $('#sensor1Status').text('Recording...')
  //               break;
  //           case msg_rec._stoppedRecording:
  //               $('#sensor1Status').text('Stopped Recording')
  //               break;
  //           default:
  //               break;
  //         } 
  //         break;
  //       case topic_subscribe.sensor2Status:
  //         switch (msg.payload) {
  //           case msg_rec._startedRecording:
  //               $('#sensor2Status').text('Started Recording')
  //               break;
  //           case msg_rec._recording:
  //               $('#sensor2Status').text('Recording...')
  //               break;
  //           case msg_rec._stoppedRecording:
  //               $('#sensor2Status').text('Stopped Recording')
  //               break;
  //           default:
  //               break;
  //         } 
  //         break;
  //     default:
  //       break;
  //   }
  // });
  // Subscribe To All Topics
  // socket.emit('subscribe',{topic:topic_subscribe.initialStatus})
  // socket.emit('subscribe',{topic:topic_subscribe.testStatus})
  // socket.emit('subscribe',{topic:topic_subscribe.doorStatus})
  // socket.emit('subscribe',{topic:topic_subscribe.liftStatus})
  // socket.emit('subscribe',{topic:topic_subscribe.sensor1Status})
  // socket.emit('subscribe',{topic:topic_subscribe.sensor2Status})

  // socket.emit('publish', {topic:topic_publish.init_status,payload:msg_pub._alive});
}); 

// 
function start_test() {
  // if(!server_online) {
  //   notifyUser('error','Cannot Start Test You Are Not Connected To Server')
  // } else if(!lift_online) {
  //   notifyUser('error','Cannot Start Test Lift Is Offline')
  // } else {
  //   socket.emit('publish', {topic:topic_publish.test,payload:msg_pub._testStart});
  //   $('#testStatus').text('')
  //   $('#doorStatus').text('')
  //   $('#liftStatus').text('')
  //   $('#sensor1Status').text('')
  //   $('#sensor2Status').text('')
  //   $('#set1Status').text('Not Started Yet')
  //   $('#set2Status').text('Not Started Yet')
  //   $('#dataSaved').html('')
  // }
  socket.emit('start_test', {'message': 'start-test'});
  
}

function stop_test() {
  socket.emit('stop_all', {'message': 'stop-test'});
}
socket.on('message_python', function(data){ 
  console.log('Python Message recieved'+ data) 
}); 

socket.on('disconnect', function(){ 
  console.log('Disconnect from server') 
}); 