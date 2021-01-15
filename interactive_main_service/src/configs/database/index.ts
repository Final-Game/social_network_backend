import { ConnectionOptions } from 'typeorm';

export const dbConnection: ConnectionOptions = {
  // type: 'postgres',
  type: 'sqlite',
  // host: process.env.POSTGRESQL_HOST,
  // port: Number(process.env.POSTGRESQL_PORT),
  // username: process.env.POSTGRESQL_USERNAME,
  // password: process.env.POSTGRESQL_PASSWORD,
  // database: process.env.POSTGRESQL_DATABASE,
  database: '/Users/kakavip/Developers/moonsmile-dev/social_network_backend/CmsAdmin/config/db/db.sqlite3',
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
