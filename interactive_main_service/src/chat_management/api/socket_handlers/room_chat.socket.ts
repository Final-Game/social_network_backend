import { Server as SocketIOServer } from 'socket.io';
import UserService from '../../../auth_management/app/services/users.service';
import { RoomSimpleDto } from '../../app/dtos/room_simple.dto';
import RoomService from '../../app/services/room.service';
import smartChatListener from '../utils/smart_chat_listener';

const roomService: RoomService = new RoomService();
const userService: UserService = new UserService();

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

  socket.on('join-smart-chat', async data => {
    const { userId } = data;

    const user: any = await userService.findUserById(userId);
    if (!user) {
      return;
    }

    const finderId = await smartChatListener.findAvailableUserMatcher(userId);
    if (finderId) {
      const room: RoomSimpleDto = await roomService.createSmartRoom(finderId, userId);

      const broadCastId: string = smartChatListener.getAvailableRoomWaiterForUserId(finderId);
      smartChatListener.notifyMatchSmartChat(broadCastId, { roomId: room.id });
    }

    return;
  });
};

export default roomChatSocket;
