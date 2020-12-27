import { InMemoryEventStorage } from 'node-cqrs';
import registerAuthDI from './auth_management/domain/di.registers';
import registerChatDI from './chat_management/domain/di.registers';
import container from './container';

function registerContainer() {
  container.register(InMemoryEventStorage, 'storage');
  registerAuthDI();
  registerChatDI();
  container.createUnexposedInstances();
}

export default registerContainer;
