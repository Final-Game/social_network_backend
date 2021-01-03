import { JobScheduler } from '../../common/jobs/scheduler.job';
import cron from 'node-cron';
import { JobListener } from '../../common/jobs/listener.job';
class CronJobScheduler implements JobScheduler {
  private listenerObservables: JobListener[];

  constructor() {
    this.listenerObservables = new Array<JobListener>();
  }

  public addListener(listener: JobListener) {
    this.listenerObservables.push(listener);
  }

  public execute() {
    this.listenerObservables.forEach(listener => listener.registerJobs());
  }
  public getTaskRunner(): any {
    return cron;
  }
}

export default CronJobScheduler;
