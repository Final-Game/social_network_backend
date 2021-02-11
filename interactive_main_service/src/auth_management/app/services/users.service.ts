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
import { AccountGateway } from '../gateways/account.gateway';
import { AccountGatewayImpl } from '../../infras/gateway_impls/account.gatewayImpl';
import { AccountInfoDto } from '../gateways/dtos/accountInfo.dto';
import { MediaAccountEntity } from '../../../chat_management/domain/entities/media_accounts.entity';
import { IMediaAccountRepository, MediaAccountRepository } from '../../../chat_management/domain/repositories/media_account.repos';
import { RunInTransaction } from '../../../common/repos/transaction';

class UserService {
  private commandBus: CommandBus;

  private userRepos: UserRepository;
  private mediaAccountRepos: IMediaAccountRepository;
  private accountGateway: AccountGateway;
  constructor() {
    this.userRepos = new UserRepository();
    this.mediaAccountRepos = new MediaAccountRepository();
    this.accountGateway = new AccountGatewayImpl();
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

  public async syncAccountInfo(account: User): Promise<void> {
    const accountInfo: AccountInfoDto = await this.accountGateway.getAccountInfo(account.refId);

    logger.info(`Account info: ${JSON.stringify(accountInfo)}`);

    // Update basic info
    account.updateData(
      accountInfo.fullName,
      accountInfo.avatar,
      accountInfo.birthDate,
      accountInfo.gender,
      accountInfo.bio,
      accountInfo.address,
      accountInfo.job,
      accountInfo.reason,
    );

    await RunInTransaction(async manager => {
      await this.userRepos.save(account);

      // Update media info
      this.mediaAccountRepos.removeMediasOfAccount(account.id);
      accountInfo.medias.forEach(async _media => {
        const _m_account = new MediaAccountEntity(account.id, _media.url, _media.type);
        await this.mediaAccountRepos.save(_m_account);
      });
    });
  }

  public async syncAllAccounts(): Promise<void> {
    const accounts: Array<User> = await this.userRepos.findAllUser();
    accounts.forEach(async account => await this.syncAccountInfo(account));
  }
}

export default UserService;
