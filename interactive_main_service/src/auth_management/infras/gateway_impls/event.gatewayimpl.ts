import axios from 'axios';
import BaseException from '../../../common/exceptions/BaseException';
import { EventGateway } from '../../app/gateways/event.gateway';

export class EventGatewayImpl implements EventGateway {
  public async matchUser(accountId: string, partnerId: string): Promise<void> {
    const matchEventUrl = `${process.env.USER_CONTENT_API_URL}/api/match_events`;

    try {
      await axios.post(`${matchEventUrl}`, {
        account_id: accountId,
        partner_id: partnerId,
      });
    } catch (error) {
      throw new BaseException(`Can't request match event`);
    }
  }
}
