import { Router } from 'express';
import UsersController from '../controllers/users.controller';
import { CreateUserDto } from '../../app/dtos/users.dto';
import Route from '../../../common/interfaces/routes.interface';
import validationMiddleware from '../../../configs/middlewares/validation.middleware';

class UsersRoute implements Route {
  public path = '/users';
  public router = Router();
  public usersController = new UsersController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
    this.router.get(`${this.path}`, this.usersController.getUsers);
    this.router.get(`${this.path}/:id(\\w+)`, this.usersController.getUserById);
    this.router.post(`${this.path}`, validationMiddleware(CreateUserDto, 'body'), this.usersController.createUser);
    // this.router.put(`${this.path}/:id(\\w+)`, validationMiddleware(CreateUserDto, 'body', true), this.usersController.updateUser);
    // this.router.delete(`${this.path}/:id(\\w+)`, this.usersController.deleteUser);
  }
}

export default UsersRoute;
