import { JobListener } from '../../common/jobs/listener.job';
import { JobScheduler } from '../../common/jobs/scheduler.job';
import { logger } from '../../common/utils/logger';
import UserService from '../app/services/users.service';

class UserJobListener implements JobListener {
  private scheduler: JobScheduler;
  private userService: UserService;

  constructor(scheduler: JobScheduler) {
    this.scheduler = scheduler;
    this.userService = new UserService();
  }

  public registerJobs() {
    const runner = this.scheduler.getTaskRunner();

    runner.schedule('0 0 * * *', () => {
      logger.debug(`Starting run task: update all accounts.`);
      this.userService.syncAllAccounts();
      logger.debug(`Finish run task: update all accounts`);
    });
    return;
  }
}

export { UserJobListener };
