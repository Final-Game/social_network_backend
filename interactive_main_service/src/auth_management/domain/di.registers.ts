import container from '../../container';
import UserAggregate from './aggregates/user.aggregate';
import UserProjection from './projections/user.projection';
import { InMemoryEventStorage } from 'node-cqrs';
function registerAuthDI() {
  container.register(InMemoryEventStorage, 'storage');
  container.registerAggregate(UserAggregate);
  container.registerProjection(UserProjection, 'users');
}

export default registerAuthDI;
