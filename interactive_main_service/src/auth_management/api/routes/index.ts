import Routes from './../../../common/interfaces/routes.interface';
import IndexRoute from './index.route';
import UsersRoute from './users.route';

const AuthManagementRoutes: Routes[] = [new IndexRoute(), new UsersRoute()];

export default AuthManagementRoutes;
