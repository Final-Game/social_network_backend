import { AccountInfoDto } from './dtos/accountInfo.dto';

export interface AccountGateway {
  getAccountInfo(accountId: string): Promise<AccountInfoDto>;
}
