import { AbstractAggregate } from 'node-cqrs';
import BaseException from '../../../common/exceptions/BaseException';
import { logger } from '../../../common/utils/logger';
import { User } from '../models/users.model';
import bcrypt from 'bcrypt';
import UserRepository from '../repositories/user.repos';
import ITestCommandPayload from './payloads/testCommand.payload';
import ICreateUserCommandPayload from './payloads/createUserCommand.payload';

class UserAggregateState {
  testEvent(event) {
    logger.info(`TestEvent created: ${JSON.stringify(event)}`);
  }
  userCreated(event) {
    logger.info(`Event userCreated: ${JSON.stringify(event)}`);
  }
}

class UserAggregate extends AbstractAggregate {
  [x: string]: any;
  static get handles() {
    return ['testCommand', 'createUserCommand'];
  }

  private userRepos: UserRepository;

  /**
   * Creates an instance of UserAggregate
   *
   * @param {object} options
   * @param {string} options.id - aggregate ID
   * @param {object[]} options.events - past aggregate events
   */
  constructor({ id, events }) {
    super({
      id,
      events,
      state: new UserAggregateState(),
    });
    this.userRepos = new UserRepository();
  }

  testCommand(_payload: ITestCommandPayload) {
    console.log(`Test command handler: ${JSON.stringify(_payload)}`);
    this.emit('testEvent', { a: 123 });
  }

  async createUserCommand(_payload: ICreateUserCommandPayload) {
    console.log(_payload);
    const findUser: User = await this.userRepos.findUserByUsername(_payload.username);
    if (findUser) throw new BaseException(`You're username ${_payload.username} already exists`);
    const hashedPassword = await bcrypt.hash(_payload.password, 10);
    const createdUser: User = await this.userRepos.save({ ..._payload, password: hashedPassword, type: 0 });
    this.emit('userCreated', { userId: createdUser.id });
  }
}

export default UserAggregate;
