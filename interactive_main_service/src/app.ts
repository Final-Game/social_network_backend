import 'reflect-metadata';
import cookieParser from 'cookie-parser';
import cors from 'cors';
import express from 'express';
import helmet from 'helmet';
import hpp from 'hpp';
import morgan from 'morgan';
import compression from 'compression';
import swaggerUi from 'swagger-ui-express';
import swaggerJSDoc from 'swagger-jsdoc';
import { createConnection } from 'typeorm';
import { dbConnection } from './configs/database';
import Routes from './common/interfaces/routes.interface';
import errorMiddleware from './configs/middlewares/error.middleware';
import { logger, stream } from './common/utils/logger';
import { createServer, Server as HTTPServer } from 'http';
import { Server as SocketIOServer } from 'socket.io';
import * as redisAdapter from 'socket.io-redis';
import registerContainer from './register.container';
import registerChatServiceSocket from './chat_management/api/socket_handlers';
import { JobScheduler } from './common/jobs/scheduler.job';
import CronJobScheduler from './configs/jobs/cronJob.scheduler';
import { UserJobListener } from './auth_management/jobs/userJob.listener';
import cacheService from './cache_service';
class App {
  public app: express.Application;
  public port: string | number;
  public env: string;
  private server: HTTPServer;
  private io: SocketIOServer;

  constructor(routes: Routes[], isBgService = false) {
    this.app = express();
    this.port = process.env.PORT || 3002;
    this.env = process.env.NODE_ENV || 'prod';
    this.server = createServer(this.app);
    this.io = new SocketIOServer(this.server, {
      cors: {
        origin: '*',
      },
    });
    this.io.adapter(redisAdapter.createAdapter(process.env.REDIS_URL));

    this.connectContainer();
    this.connectToDatabase();
    this.initializeMiddlewares();
    this.initializeRoutes(routes);
    this.initializeSwagger();
    this.initializeErrorHandling();
    this.handleSocketConnection();
    this.initializeCache();
    if (isBgService) {
      this.handleBackgroundJobs();
    }
  }

  public listen() {
    this.server.listen(this.port, () => {
      logger.info(`🚀 App listening on the port ${this.port}`);
    });
  }

  public getServer() {
    return this.server;
  }

  private connectToDatabase() {
    createConnection(dbConnection)
      .then(() => {
        logger.info('🟢 The REST database is connected.');
      })
      .catch((error: Error) => {
        logger.error(`🔴 Unable to connect to the REST database: ${error}.`);
      });
  }

  private initializeMiddlewares() {
    if (this.env === 'prod') {
      this.app.use(morgan('combined', { stream }));
      this.app.use(cors({ origin: 'your.domain.com', credentials: true }));
    } else if (this.env === 'development') {
      this.app.use(morgan('dev', { stream }));
      this.app.use(cors({ origin: true, credentials: true }));
    }

    this.app.use(hpp());
    this.app.use(helmet());
    this.app.use(compression());
    this.app.use(express.json());
    this.app.use(express.urlencoded({ extended: true }));
    this.app.use(cookieParser());
  }

  private initializeRoutes(routes: Routes[]) {
    routes.forEach(route => {
      this.app.use('/', route.router);
    });
  }

  private async initializeCache() {
    cacheService.register();
  }

  private initializeSwagger() {
    const options = {
      swaggerDefinition: {
        info: {
          title: 'REST API',
          version: '1.0.0',
          description: 'Example docs',
        },
      },
      apis: ['swagger.yaml'],
    };

    const specs = swaggerJSDoc(options);
    this.app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(specs));
  }

  private initializeErrorHandling() {
    this.app.use(errorMiddleware);
  }

  private connectContainer() {
    registerContainer();
  }

  private handleBackgroundJobs() {
    const jobScheduler: JobScheduler = new CronJobScheduler();
    jobScheduler.addListener(new UserJobListener(jobScheduler));
    jobScheduler.execute();
  }

  private handleSocketConnection() {
    this.io.on('connection', socket => {
      logger.info('A user connected');
      registerChatServiceSocket(this.io, socket);

      socket.on('hello', data => {
        logger.info(data);

        const roomId: string = data['roomId'];
        socket.join(roomId);

        this.io.in(roomId).emit('hello', 'Hello worlds!');
      });
      socket.on('disconnect', () => {
        logger.info(`User ${socket.id} disconnected`);
      });
    });
    this.io.on('connect', socket => {
      logger.info(`On connect: ${socket.id}`);
    });
  }
}

export default App;
