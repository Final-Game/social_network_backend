import { ICache } from './cache';
import * as redis from 'redis';
import * as asyncRedis from 'async-redis';
export class RedisCache implements ICache {
  private _cacheClient = null;
  public register() {
    const client = redis.createClient(process.env.REDIS_URI);
    this._cacheClient = asyncRedis.decorate(client);
  }

  public async set(key: string, data: any, timeout: number): Promise<boolean> {
    console.log(`Set cache: key ${key} - value ${data}`);
    return await this._cacheClient.setex(key, timeout, data);
  }

  public async get(key: string): Promise<any> {
    return await this._cacheClient.get(key);
  }
}
