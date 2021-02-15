import { Server as SocketIOServer } from 'socket.io';

import roomChatSocket from './room_chat.socket';

const registerChatServiceSocket = (io: SocketIOServer, socket: any) => {
  roomChatSocket(io, socket);
};

export default registerChatServiceSocket;
