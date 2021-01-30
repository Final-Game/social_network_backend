import { EntityManager, getConnection, getManager, Transaction, TransactionManager } from 'typeorm';
import BaseException from '../../../common/exceptions/BaseException';
import { UserEntity } from '../entities/users.entity';
import { User } from '../models/users.model';

class UserRepository {
  private model = UserEntity;

  @Transaction()
  public async findAllUser(@TransactionManager() manager: EntityManager = getManager()): Promise<User[]> {
    return await manager.find(this.model);
  }

  public async findUserById(userId: string, raiseException = false): Promise<User> {
    const manager = getConnection().manager;

    const user: User = await manager.findOne(this.model, { where: { id: userId } });
    if (raiseException && !user) throw new BaseException(`Can't find user with id: ${userId}`);
    return user;
  }

  public async findAccountByBaseAccountId(baseId: string, raiseException = false): Promise<User> {
    const manager = getConnection().manager;

    const account: User = await manager.findOne(this.model, { where: { refId: baseId } });

    if (raiseException && !account) {
      throw new BaseException(`Can't find account with ref id: ${baseId}`);
    }
    return account;
  }

  public async getOrCreateAccountByBaseAccountId(baseId: string): Promise<User> {
    let account: User = await this.findAccountByBaseAccountId(baseId, false);

    if (!account) {
      account = await this.save(new UserEntity(baseId));
    }

    return account;
  }

  public async findUserByUsername(username: string, raiseException = false): Promise<User> {
    const manager = getConnection().manager;

    const user = await manager.findOne(this.model, { where: { username: username } });

    if (!user && raiseException) {
      throw new BaseException(`Can't find user with username: ${username}`);
    }

    return user;
  }

  public async save(user): Promise<User> {
    const manager = getConnection().manager;
    return await manager.save(this.model, user);
  }
}

export default UserRepository;
