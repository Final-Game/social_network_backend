import { ConnectionOptions } from 'typeorm';

export const dbConnection: ConnectionOptions = {
  type: 'mysql',
  host: process.env.DB_HOST,
  port: Number.parseInt(process.env.DB_PORT || '3306'),
  username: process.env.DB_USERNAME,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE,
  synchronize: false,
  logging: false,
  entities: [process.env.NODE_ENV !== 'local' ? 'build/*/domain/entities/*{.ts,.js}' : 'src/*/domain/entities/*{.ts,.js}'],
  migrations: [process.env.NODE_ENV !== 'local' ? 'build/migration/*{.ts,.js}' : 'src/*/infras/migration/*{.ts,.js}'],
  subscribers: [process.env.NODE_ENV !== 'local' ? 'build/subscriber/*{.ts,.js}' : 'src/subscriber/*{.ts,.js}'],
  cli: {
    entitiesDir: 'src/entity',
    migrationsDir: 'src/migration',
    subscribersDir: 'src/subscriber',
  },
};
