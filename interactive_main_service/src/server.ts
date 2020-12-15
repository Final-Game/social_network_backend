import 'dotenv/config';
import App from './app';
import AuthManagementRoutes from './auth_management/api/routes';
import validateEnv from './common/utils/validateEnv';

validateEnv();

const app = new App(AuthManagementRoutes);

app.listen();
