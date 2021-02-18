import dotenv from 'dotenv';
import App from './app';
import AuthManagementRoutes from './auth_management/api/routes';
import validateEnv from './common/utils/validateEnv';
import cluster from 'cluster';
import os from 'os';
import GrpcApp from './grpc.app';
import { chatModuleHandler } from './chat_management/api/msg_handlers';
import path from 'path';
import { logger } from './common/utils/logger';

function runGrpc() {
  const protoHandlers = chatModuleHandler;
  const grpcApp = new GrpcApp(protoHandlers);
  grpcApp.listen();
}

function runRest(isBgService = false) {
  const app = new App(AuthManagementRoutes, isBgService);
  app.listen();
}

function loadEnv() {
  dotenv.config({ path: path.join(__dirname, `./configs/envs/${process.env.NODE_ENV}.env`) });

  validateEnv();
}

function main() {
  loadEnv();

  const isDebugGRPC = process.env.DEBUG_GRPC === 'true';
  const isDebugREST = process.env.DEBUG_REST === 'true';

  if (isDebugGRPC) {
    runGrpc();
  } else if (isDebugREST) {
    runRest();
  } else {
    if (cluster.isMaster) {
      const numCPUs = os.cpus().length;
      logger.debug(`Master ${process.pid} is running`);

      // Fork workers.
      for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
      }

      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      cluster.on('exit', (worker, _code, _signal) => {
        logger.debug(`worker ${worker.process.pid} died`);
      });
    } else {
      if (cluster.worker.id === 1) {
        runGrpc();
        runRest(true);
      } else {
        runRest();
      }
    }
  }
}

main();
