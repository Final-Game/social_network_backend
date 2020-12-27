import { loadSync } from '@grpc/proto-loader';
import grpc from 'grpc';

const protoLoader = (protoPath: string) => {
  const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
  };

  const packageDefinition = loadSync(protoPath, options);
  return grpc.loadPackageDefinition(packageDefinition);
};

export default protoLoader;
