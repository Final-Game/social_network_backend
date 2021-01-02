import { Server as SocketIOServer } from 'socket.io';
import UserService from '../../../auth_management/app/services/users.service';

class SmartChatListener {
  userService: UserService;
  available_user_ids: Array<string>;
  socket: any;
  io: SocketIOServer;

  constructor() {
    this.userService = new UserService();
    this.available_user_ids = new Array<string>();
  }

  public register(io: SocketIOServer, socket: any) {
    this.io = io;
    this.socket = socket;
  }

  public addNewWaitingUser(userId: string) {
    this.available_user_ids.push(userId);

    // create room owner for waiting matcher
    this.socket.join(this.getAvailableRoomWaiterForUserId(userId));
  }

  public getAvailableRoomWaiterForUserId(userId: string): string {
    return `${userId}-room-waiter`;
  }

  public removeWaitingUser(userId: string) {
    this.available_user_ids = this.available_user_ids.filter(item => item != userId);
  }

  public async findAvailableUserMatcher(upComingPartnerId: string): Promise<string | null> {
    for (let idx = 0; idx < this.available_user_ids.length; idx++) {
      const finderId = this.available_user_ids[idx];

      if (await this.userService.checkUserCanMatch(finderId, upComingPartnerId)) {
        this.socket.join(this.getAvailableRoomWaiterForUserId(finderId));
        this.removeWaitingUser(finderId);

        return finderId;
      }
    }

    this.addNewWaitingUser(upComingPartnerId);
    return null;
  }

  public notifyMatchSmartChat(broadCastId: string, data: any) {
    this.io.to(broadCastId).emit('find-smart-chat-success', data);
  }
}

const smartChatListener: SmartChatListener = new SmartChatListener();

export default smartChatListener;
