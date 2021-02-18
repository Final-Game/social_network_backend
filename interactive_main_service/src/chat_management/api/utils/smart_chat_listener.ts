import UserService from '../../../auth_management/app/services/users.service';
import cacheService from '../../../cache_service';
import { logger } from '../../../common/utils/logger';

class SmartChatListener {
  userService: UserService;

  constructor() {
    this.userService = new UserService();
  }

  public async getAvailableUserIds(): Promise<Array<string>> {
    return JSON.parse(await cacheService.get('available_user_ids')) || [];
  }

  public async addNewAvailableUserId(userId: string) {
    const available_user_ids: Array<string> = await this.getAvailableUserIds();
    available_user_ids.push(userId);

    await cacheService.set('available_user_ids', JSON.stringify(available_user_ids), 5 * 60);
  }

  public async addNewWaitingUser(userId: string) {
    logger.debug(`User ${userId} is waiting for smart chat.`);
    await this.addNewAvailableUserId(userId);
  }

  public getAvailableRoomWaiterForUserId(userId: string): string {
    return `${userId}-room-waiter`;
  }

  public async removeWaitingUser(userId: string) {
    const available_user_ids = await this.getAvailableUserIds();
    await cacheService.set('available_user_ids', JSON.stringify(available_user_ids.filter(item => item != userId)), 5 * 60);
  }

  public async findAvailableUserMatcher(upComingPartnerId: string): Promise<string | null> {
    const available_user_ids = await this.getAvailableUserIds();
    logger.info(`Clients are waiting: ${available_user_ids}`);
    for (let idx = 0; idx < available_user_ids.length; idx++) {
      const finderId = available_user_ids[idx];

      if (await this.userService.checkUserCanMatch(finderId, upComingPartnerId)) {
        logger.info(`User ${upComingPartnerId} is matching with user ${finderId}`);
        await this.removeWaitingUser(finderId);

        return finderId;
      }
    }

    await this.addNewWaitingUser(upComingPartnerId);
    return null;
  }
}

const smartChatListener: SmartChatListener = new SmartChatListener();

export default smartChatListener;
