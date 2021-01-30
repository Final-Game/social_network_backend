import grpc from 'grpc';

export class GrpcInternalError {
  public code: number;
  public message: string;

  constructor(message: string) {
    this.message = message;
    this.code = grpc.status.INTERNAL;
  }
}
