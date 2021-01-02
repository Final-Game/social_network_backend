import { Server as SocketIOServer } from 'socket.io';
import smartChatListener from '../utils/smart_chat_listener';

import roomChatSocket from './room_chat.socket';

const registerChatServiceSocket = (io: SocketIOServer, socket: any) => {
  smartChatListener.register(io, socket);

  roomChatSocket(io, socket);
};

export default registerChatServiceSocket;
