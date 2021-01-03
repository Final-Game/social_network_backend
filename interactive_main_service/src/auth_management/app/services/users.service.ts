import { getRepository, Repository } from 'typeorm';
import bcrypt from 'bcrypt';
import { CreateUserDto } from '../dtos/users.dto';
import HttpException from '../../../common/exceptions/HttpException';
import { User } from '../../domain/models/users.model';
import { UserEntity } from '../../domain/entities/users.entity';
import { isEmpty } from '../../../common/utils/util';
import UserRepository from '../../domain/repositories/user.repos';
import container from '../../../container';
import { logger } from '../../../common/utils/logger';
import { CommandBus } from 'node-cqrs';
import ITestCommandPayload from '../../domain/aggregates/payloads/testCommand.payload';
import CreateUserCommandPayload from '../../domain/aggregates/payloads/createUserCommand.payload';

class UserService {
  private commandBus: CommandBus;

  private userRepos: UserRepository;
  constructor() {
    this.userRepos = new UserRepository();
    this.commandBus = container.commandBus;
  }

  public async findAllUser(): Promise<User[]> {
    const users: User[] = await this.userRepos.findAllUser();

    // const payload: ITestCommandPayload = {
    //   test: 'xyz',
    // };

    // await this.commandBus.send('testCommand', undefined, { payload });

    // container.eventStore.once('testEvent', event => {
    //   logger.info(`User aggregate created with ID ${event.aggregateId}`);
    // });
    return users;
  }

  public async findUserById(userId: string): Promise<User> {
    return this.userRepos.findUserById(userId, true);
  }

  public async getOrCreateAccountByAccountId(accountBaseId: string): Promise<User> {
    let account: User = await this.userRepos.findAccountByBaseAccountId(accountBaseId, false);

    if (!account) {
      // TODO verify account before create

      account = await this.userRepos.save(new UserEntity(accountBaseId));
    }
    return account;
  }

  public async createUser(userData: CreateUserDto): Promise<User> {
    const payload = { username: userData.username, password: userData.password };

    const data = await this.commandBus.send('createUserCommand', undefined, { payload });

    container.eventStore.once('userCreated', event => {
      logger.info(`User aggregate created with ID ${event.aggregateId}`);
    });
    const userId: string = data[0].payload.userId;
    return this.userRepos.findUserById(userId);
  }

  public async checkUserCanMatch(userAId: string, userBId: string): Promise<boolean> {
    const userA: User = await this.userRepos.findUserById(userAId, true);
    const userB: User = await this.userRepos.findUserById(userBId, true);

    return userA.canMatch(userB) && userB.canMatch(userA);
  }
}

export default UserService;
