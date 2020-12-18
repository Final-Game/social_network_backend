class BaseException extends Error {
  public message: string;
  public errorCode: string;
  public status: number;

  constructor(message: string, errorCode = 'base_exception', status = 500) {
    super(message);
    this.message = message;
    this.errorCode = errorCode;
    this.status = status;
  }
}

export default BaseException;
