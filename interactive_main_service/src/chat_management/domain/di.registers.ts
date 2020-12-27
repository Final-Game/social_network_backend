import container from '../../container';
import MatchAggregate from './aggregates/match.aggregate';

function registerChatDI() {
  container.registerAggregate(MatchAggregate);
}

export default registerChatDI;
