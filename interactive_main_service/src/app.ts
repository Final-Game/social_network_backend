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
import registerAuthDI from './auth_management/domain/di.registers';
import container from './container';
import { createServer, Server as HTTPServer } from 'http';
import { Server as SocketIOServer } from 'socket.io';

class App {
  public app: express.Application;
  public port: string | number;
  public env: string;
  private server: HTTPServer;
  private io: SocketIOServer;

  constructor(routes: Routes[]) {
    this.app = express();
    this.port = process.env.PORT || 3000;
    this.env = process.env.NODE_ENV || 'production';
    this.server = createServer(this.app);
    this.io = new SocketIOServer(this.server);

    this.connectContainer();
    this.connectToDatabase();
    this.initializeMiddlewares();
    this.initializeRoutes(routes);
    this.initializeSwagger();
    this.initializeErrorHandling();
    this.handleSocketConnection();
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
        logger.info('🟢 The database is connected.');
      })
      .catch((error: Error) => {
        logger.error(`🔴 Unable to connect to the database: ${error}.`);
      });
  }

  private initializeMiddlewares() {
    if (this.env === 'production') {
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

  private initializeSwagger() {
    const options = {
      swaggerDefinition: {
        info: {
          title: 'REST API',
          version: '1.0.0',
          description: 'Example docs',
        },
      },o
      apis: ['swagger.yaml'],
    };

    const specs = swaggerJSDoc(options);
    this.app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(specs));
  }

  private initializeErrorHandling() {
    this.app.use(errorMiddleware);
  }

  private connectContainer() {
    registerAuthDI();
    container.createUnexposedInstances();
  }

  private handleSocketConnection() {
    this.io.on('connection', socket => {
      console.log('A user connected');
      console.log(socket.rooms);

      socket.on('join-room', data => {
        const userId: string = data['userId'];
        const roomId: string = data['roomId'];

        // Validate user can join current room

        socket.join(roomId);
        console.log(`Joined to room: ${roomId}`);
      });

      socket.on('message', data => {
        console.log(data);
        // socket.broadcast.emit('message', {
        //   data: data,
        // });

        const roomId: string = data.roomId;

        socket.to(roomId).emit('hello', 'Nguyen Minh Tuan');
      });
      socket.on('disconnect', () => {
        console.log(`User ${socket.id} disconnected`);
      });
    });
    this.io.on('connect', socket => {
      console.log(`On connect: ${socket.id}`);
    });
  }
}

export default App;
