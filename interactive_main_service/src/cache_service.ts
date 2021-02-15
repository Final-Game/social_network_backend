import { ICache } from './common/caches/cache';
import { RedisCache } from './common/caches/redis.cache';

const cacheService: ICache = new RedisCache();

export default cacheService;
