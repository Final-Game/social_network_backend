import grpc, { Server as GrpcServer } from 'grpc';
import { logger } from './common/utils/logger';
import path from 'path';
import {loadSync} from '@grpc/proto-loader';
import registerContainer from './register.container';
import { createConnection } from 'typeorm';
import { dbConnection } from './configs/database';

function sayHello(call, callback) {
  callback(null, { message: 'Hello ' + call.request.name });
}

class GrpcApp {
  private server: GrpcServer;

  constructor() {
    this.server = new GrpcServer();
    this.loadProtos();
    this.connectToDatabase();
    this.connectContainer();
  }

  public listen() {
    this.server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
      this.server.start();
      logger.info('🚀 gRPC App listening on the port 50051');
    });
  }

  private loadProtos() {
    const HELLO_PROTO_PATH = path.join(__dirname, './../../protos/hello.proto');

    const options = {
      keepCase: true,
      longs: String,
      enums: String,
      defaults: true,
      oneofs: true,
    };
    const packageDefinition = loadSync(HELLO_PROTO_PATH, options);

    const hello_proto: any = grpc.loadPackageDefinition(packageDefinition).helloworld;

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
