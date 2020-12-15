import { Container, InMemoryEventStorage } from 'node-cqrs';

const container = new Container();

container.register(InMemoryEventStorage, 'storage');
container.createUnexposedInstances();
export default container;
