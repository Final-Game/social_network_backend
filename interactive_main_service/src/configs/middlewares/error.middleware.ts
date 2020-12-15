import { NextFunction, Request, Response } from 'express';
import HttpException from '../../common/exceptions/HttpException';
import { logger } from '../../common/utils/logger';

const errorMiddleware = (error: HttpException, req: Request, res: Response, next: NextFunction) => {
  try {
    const status: number = error.status || 500;
    const message: string = error.message || 'Something went wrong';
    const errorCode: string = error.errorCode || '';

    logger.error(`StatusCode : ${status}, Message : ${message}`);
    res.status(status).json({ message, errorCode });
  } catch (_e) {
    next(_e);
  }
};

export default errorMiddleware;
