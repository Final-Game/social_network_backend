import container from '../../container';
import UserAggregate from './aggregates/user.aggregate';
import UserProjection from './projections/user.projection';

function registerAuthDI() {
  container.registerAggregate(UserAggregate);
  container.registerProjection(UserProjection, 'users');
}

export default registerAuthDI;
