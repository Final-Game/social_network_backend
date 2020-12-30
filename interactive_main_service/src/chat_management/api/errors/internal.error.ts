import grpc from 'grpc';

export class GrpcInternalError {
  public code: number;
  public status: number;
  public message: string;

  constructor(message: string) {
    this.message = message;

    this.code = 500;
    this.status = grpc.status.INTERNAL;
  }
}
