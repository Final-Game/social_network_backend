import { Server as SocketIOServer } from 'socket.io';
import UserService from '../../../auth_management/app/services/users.service';
import { User } from '../../../auth_management/domain/models/users.model';
import BaseException from '../../../common/exceptions/BaseException';
import { logger } from '../../../common/utils/logger';
import { RoomSimpleDto } from '../../app/dtos/room_simple.dto';
import RoomService from '../../app/services/room.service';
import { RoomType } from '../../domain/enums/roomType.enum';
import smartChatListener from '../utils/smart_chat_listener';

const roomService: RoomService = new RoomService();
const userService: UserService = new UserService();

async function getAccountReference(accountId: string): Promise<User> {
  const user: User = await userService.getOrCreateAccountByAccountId(accountId);
  if (!user) {
    throw new BaseException("Can't find account.");
  }
  return user;
}

const roomChatSocket = (io: SocketIOServer, socket: any) => {
  socket.on('join-room', async data => {
    const userId: string = data['userId'];
    const roomId: string = data['roomId'];

    // Validate user can join current room
    const account = await getAccountReference(userId);
    if (!(await roomService.checkAccountInRoomType(account.id, roomId, RoomType.NORMAL))) {
      throw new BaseException(`Account ${account.refId} can't join this room.`);
    }

    socket.join(roomId);
    logger.info(`UserId: ${userId} joined to room: ${roomId}`);

    io.sockets.in(roomId).emit('new-mem-joined', { accountId: account.refId });
    logger.info(`Notify new member ${account.refId} join room ${roomId} to other members.`);
  });

  socket.on('join-smart-room', async data => {
    const { accountId, roomId } = data;

    // validate user can join smart room
    const account = await getAccountReference(accountId);
    if (!(await roomService.checkAccountInRoomType(account.id, roomId, RoomType.SMART))) {
      throw new BaseException(`Account ${account.refId} isn't existed in this room.`);
    }
    // join room.
    socket.join(roomId);
    console.log(`User ${account.refId} joined to room ${roomId}`);

    io.to(roomId).emit('new-mem-joined-smart-chat', { accountId: account.refId });
  });

  socket.on('send-msg', async data => {
    const { roomId, senderId, message } = data;
    const { content } = message;
    const sender = await getAccountReference(senderId);

    roomService.sendMessage(sender.id, roomId, { content: content });

    io.to(roomId).emit('new-msg', { accountId: sender.refId, message: { content: content } });
  });

  socket.on('send-smart-msg', async data => {
    const { roomId, senderId, message } = data;
    const { content } = message;

    socket.join(roomId);

    const sender = await getAccountReference(senderId);

    roomService.sendSmartMsg(sender.id, roomId, { content: content });

    io.to(roomId).emit('new-smart-msg', { accountId: sender.id, message: { content: content } });
  });

  socket.on('find-smart-chat', async data => {
    let { accountId } = data;
    accountId = (await getAccountReference(accountId)).id;

    const finderId = await smartChatListener.findAvailableUserMatcher(accountId);
    if (finderId) {
      socket.join(smartChatListener.getAvailableRoomWaiterForUserId(finderId));

      const room: RoomSimpleDto = await roomService.createSmartRoom(finderId, accountId);
      const broadCastId: string = smartChatListener.getAvailableRoomWaiterForUserId(finderId);

      // notify data.
      io.to(broadCastId).emit('find-smart-chat-success', { roomId: room.id });
    } else {
      socket.join(smartChatListener.getAvailableRoomWaiterForUserId(accountId));
    }

    return;
  });

  socket.on('exit-smart-chat', async data => {
    const account = await getAccountReference(data['accountId']);
    await smartChatListener.removeWaitingUser(account.id);
  });
};

export default roomChatSocket;
