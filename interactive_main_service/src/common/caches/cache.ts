export interface ICache {
  register: () => any;

  set: (key: string, data: any, timeout: number) => Promise<boolean>;
  get: (key: string) => Promise<any>;
}
