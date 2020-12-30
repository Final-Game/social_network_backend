import { Server as SocketIOServer } from 'socket.io';
import RoomService from '../../app/services/room.service';

const roomService: RoomService = new RoomService();

const roomChatSocket = (io: SocketIOServer, socket: any) => {
  socket.on('join-room', data => {
    const userId: string = data['userId'];
    const roomId: string = data['roomId'];

    // Validate user can join current room

    socket.join(roomId);
    console.log(`Joined to room: ${roomId}`);

    io.to(roomId).emit('new-mem-joined', { userId: userId });
  });

  socket.on('send-msg', data => {
    const { roomId, senderId, message } = data;
    const { content, media } = message;
    const { mediaUrl, type } = media;

    roomService.sendMessage(senderId, roomId, { content: content, media: { mediaUrl: mediaUrl, type: type } });
  });
};

export default roomChatSocket;
