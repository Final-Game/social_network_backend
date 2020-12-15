class BaseException extends Error {
  public message: string;
  public errorCode: string;

  constructor(message: string, errorCode = 'base_exception') {
    super(message);
    this.message = message;
    this.errorCode = errorCode;
  }
}

export default BaseException;
