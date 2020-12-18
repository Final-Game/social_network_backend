import { NextFunction, Request, Response } from 'express';
import BaseException from '../../common/exceptions/BaseException';
import { logger } from '../../common/utils/logger';

const errorMiddleware = (error: BaseException, req: Request, res: Response, next: NextFunction) => {
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
