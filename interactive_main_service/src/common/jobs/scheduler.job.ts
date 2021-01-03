import { JobListener } from './listener.job';

export interface JobScheduler {
  addListener: (listener: JobListener) => void;
  execute: () => void;
  getTaskRunner: () => any;
}
