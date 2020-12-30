import 'dotenv/config';
import App from './app';
import AuthManagementRoutes from './auth_management/api/routes';
import validateEnv from './common/utils/validateEnv';
import cluster from 'cluster';
import os from 'os';
import GrpcApp from './grpc.app';
import { chatModuleHandler } from './chat_management/api/msg_handlers';

validateEnv();

function runGrpc() {
  const protoHandlers = chatModuleHandler;
  const grpcApp = new GrpcApp(protoHandlers);
  grpcApp.listen();
}

function runRest() {
  const app = new App(AuthManagementRoutes);
  app.listen();
}

const isDebugGRPC = process.env.DEBUG_GRPC === 'true';
const isDebugREST = process.env.DEBUG_REST === 'true';

if (isDebugGRPC) {
  runGrpc();
} else if (isDebugREST) {
  runRest();
} else {
  if (cluster.isMaster) {
    const numCPUs = os.cpus().length;
    console.log(`Master ${process.pid} is running`);

    // Fork workers.
    for (let i = 0; i < numCPUs; i++) {
      cluster.fork();
    }

    cluster.on('exit', (worker, code, signal) => {
      console.log(`worker ${worker.process.pid} died`);
    });
  } else {
    if (cluster.worker.id === 1) {
      runGrpc();
    } else {
      runRest();
    }
  }
}
