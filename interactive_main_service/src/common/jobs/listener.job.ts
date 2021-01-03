import { JobScheduler } from './scheduler.job';

export interface JobListener {
  registerJobs: () => void;
}
