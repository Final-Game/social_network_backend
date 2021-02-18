import { AccountInfoDto } from './dtos/accountInfo.dto';
import { AccountReportDto } from './dtos/accountReport.dto';

export interface AccountGateway {
  getAccountInfo(accountId: string): Promise<AccountInfoDto>;
  reportUser(accountId: string, dto: AccountReportDto): Promise<void>;
}
