import 'dotenv/config';
import App from './app';
import AuthManagementRoutes from './auth_management/api/routes';
import validateEnv from './common/utils/validateEnv';
import cluster from 'cluster';
import os from 'os';
import GrpcApp from './grpc.app';
import { chatHandlers } from './chat_management/api/msg_handlers';

validateEnv();

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
    const protoHandlers = chatHandlers;
    const grpcApp = new GrpcApp(protoHandlers);
    grpcApp.listen();
  } else {
    const app = new App(AuthManagementRoutes);
    app.listen();
  }
}
