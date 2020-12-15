import Routes from './../../../common/interfaces/routes.interface';
import AuthRoute from './auth.route';
import IndexRoute from './index.route';
import UsersRoute from './users.route';

const AuthManagementRoutes: Routes[] = [new IndexRoute(), new UsersRoute(), new AuthRoute()];

export default AuthManagementRoutes;
