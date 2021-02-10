import io from 'socket.io-client';

const args = process.argv.slice(2);
console.log(`Args pass: ${args}`);
const accountId = args[0];

const socket = io('http://127.0.0.1:3002', { transports: ['websocket'], rejectUnauthorized: false, secure: true });

// socket.on('connect', () => {
//   console.log(socket.id); // x8WIv7-mJelg7on_ALbx
// });

function runEventListener(socket) {
  socket.on('new-mem-joined', function (data) {
    console.log(`new member joined: ${JSON.stringify(data)}`);
  });
  socket.on('find-smart-chat-success', function (data) {
    console.log(`Smart chat create for: ${JSON.stringify(data)}`);

    const roomId = data['roomId'];

    const sendSmartMsgData = { senderId: accountId, roomId: roomId, message: { content: 'What the fuck.' } };
    socket.emit('send-smart-msg', sendSmartMsgData);
  });

  socket.on('new-smart-msg', function (data) {
    console.log(`New smart chat message: ${JSON.stringify(data)}`);
  });
}

runEventListener(socket);
const data = { userId: accountId, roomId: '10lmzXhC6PV58lxCAAAB' };
socket.emit('hello', data => {
  console.log('Nguyen Minh Tuan');
});
// socket.emit('join-room', data);
// const sendMsgData = {
//   roomId: 'd08e91e8-f982-48a1-ba57-cfa6ff795dde',
//   senderId: 'fe2e8f63-e283-48f0-ae59-3451a5fc7b45',
//   message: { content: 'this is me', media: { mediaUrl: 'this is mediaUrl', type: 1 } },
// };
// socket.emit('send-msg', sendMsgData);

// const testSmartChatData = { accountId: accountId };
// socket.emit('find-smart-chat', testSmartChatData);

// function freeze(time) {
//   const stop = new Date().getTime() + time;
//   while (new Date().getTime() < stop);
// }

// while (1 < 2) {
//   console.log(`waiting for connection.`);
//   freeze(3000);
// }
