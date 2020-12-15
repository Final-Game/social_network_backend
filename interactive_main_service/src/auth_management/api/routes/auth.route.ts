import { Router } from 'express';
import AuthController from '../controllers/auth.controller';
import { CreateUserDto } from '../../app/dtos/users.dto';
import Route from '../../../common/interfaces/routes.interface';
import authMiddleware from '../../../configs/middlewares/auth.middleware';
import validationMiddleware from '../../../configs/middlewares/validation.middleware';

class AuthRoute implements Route {
  public router = Router();
  public authController = new AuthController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
    this.router.post('/signup', validationMiddleware(CreateUserDto, 'body'), this.authController.signUp);
    this.router.post('/login', validationMiddleware(CreateUserDto, 'body'), this.authController.logIn);
    this.router.post('/logout', authMiddleware, this.authController.logOut);
  }
}

export default AuthRoute;
