import { AccountGateway } from '../../app/gateways/account.gateway';
import { AccountInfoDto } from '../../app/gateways/dtos/accountInfo.dto';
import axios from 'axios';
import BaseException from '../../../common/exceptions/BaseException';

export class AccountGatewayImpl implements AccountGateway {
  public async getAccountInfo(accountId: string): Promise<AccountInfoDto> {
    const getAccountUrl = `${process.env.USER_CONTENT_API_URL}/api/accounts/${accountId}/info`;

    try {
      const res = await axios.get(`${getAccountUrl}`);

      const data_response: any = res.data;
      return new AccountInfoDto(
        data_response['id'],
        data_response['full_name'],
        data_response['avatar'],
        data_response['birth_date'],
        data_response['gender'] || 0,
        data_response['bio'] || '',
        data_response['address'] || '',
        data_response['job'] || '',
        data_response['reason'] || '',
      );
    } catch (error) {
      throw new BaseException(`Can't request get account info: ${error.message}`);
    }
  }
}
