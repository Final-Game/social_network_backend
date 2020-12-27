import { CommandBus } from 'node-cqrs';
import UserRepository from '../../../auth_management/domain/repositories/user.repos';
import { logger } from '../../../common/utils/logger';
import container from '../../../container';
import { Match } from '../../domain/models/matches.model';
import { IMatchRepository, MatchRepository } from '../../domain/repositories/match.repos';
import { CreateMatchDto } from '../dtos/matches.dto';

class MatchService {
  private commandBus: CommandBus;
  private matchRepos: IMatchRepository;
  private userRepos: UserRepository;

  constructor() {
    this.commandBus = container.commandBus;
    this.matchRepos = new MatchRepository();
    this.userRepos = new UserRepository();
  }

  public async createMatch(data: CreateMatchDto): Promise<Match> {
    const sender = await this.userRepos.findUserById(data.accountId, true);
    const receiver = await this.userRepos.findUserById(data.dto.receiverId, true);

    const payload = {
      senderId: sender.id,
      dto: {
        receiverId: receiver.id,
        status: data.dto.status,
      },
    };

    data = await this.commandBus.send('createMatchCommand', undefined, { payload });
    container.eventStore.once('matchCreatedEvent', event => {
      logger.info(`Match aggregate created with ID ${event.aggregateId}`);
    });

    console.log(data);
    return;
  }
}

export default MatchService;
