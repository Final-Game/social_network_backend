import grpc, { Server as GrpcServer } from 'grpc';
import { logger } from './common/utils/logger';
import registerContainer from './register.container';
import { createConnection } from 'typeorm';
import { dbConnection } from './configs/database';
import protoLoader from './common/grpc/protoLoader';
import { HELLO_PROTO_PATH } from './common/grpc/contants';

function sayHello(call, callback) {
  callback(null, { message: 'Hello ' + call.request.name });
}

class GrpcApp {
  private server: GrpcServer;
  private port: string | number;

  constructor(protoHandlers: Array<any>) {
    this.server = new GrpcServer();
    this.port = process.env.GRPC_PORT || 50051;
    this.loadProtos(protoHandlers);
    this.connectToDatabase();
    this.connectContainer();
  }

  public listen() {
    this.server.bindAsync(`0.0.0.0:${this.port}`, grpc.ServerCredentials.createInsecure(), () => {
      this.server.start();
      logger.info(`🚀 gRPC App listening on the port ${this.port}`);
    });
  }

  private loadProtos(handlers: Array<any>) {
    const hello_proto: any = protoLoader(HELLO_PROTO_PATH).helloworld;

    for (let idx = 0; idx < handlers.length; idx++) {
      const element: any = handlers[idx];
      this.server.addService(element.key, element.value);
    }

    this.server.addService(hello_proto.Greeter.service, { sayHello: sayHello });
    return;
  }

  private connectContainer() {
    registerContainer();
  }

  private connectToDatabase() {
    createConnection(dbConnection)
      .then(() => {
        logger.info('🟢 The gRPC database is connected.');
      })
      .catch((error: Error) => {
        logger.error(`🔴 Unable to connect to the gRPC database: ${error}.`);
      });
  }
}

export default GrpcApp;
