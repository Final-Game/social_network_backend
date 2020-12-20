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

  public async createUser(userData: CreateUserDto): Promise<User> {
    const payload = { username: userData.username, password: userData.password };

    const data = await this.commandBus.send('createUserCommand', undefined, { payload });

    container.eventStore.once('userCreated', event => {
      logger.info(`User aggregate created with ID ${event.aggregateId}`);
    });
    const userId: string = data[0].payload.userId;
    return this.userRepos.findUserById(userId);
  }

  // public async updateUser(userId: string, userData: User): Promise<User> {
  //   // if (isEmpty(userData)) throw new HttpException(400, "You're not userData");
  //   // const findUser: User = await this.userRepos.findOne({ where: { id: userId } });
  //   // if (!findUser) throw new HttpException(409, "You're not user");
  //   // const hashedPassword = await bcrypt.hash(userData.password, 10);
  //   // await this.userRepos.update(userId, { ...userData, password: hashedPassword });
  //   // const updateUser: User = await this.userRepos.findOne({ where: { id: userId } });
  //   // return updateUser;
  // }

  // public async deleteUser(userId: string): Promise<User> {
  //   // const findUser: User = await this.userRepos.findOne({ where: { id: userId } });
  //   // if (!findUser) throw new HttpException(409, "You're not user");
  //   // await this.userRepos.delete({ id: userId });
  //   // return findUser;
  // }
}

export default UserService;
