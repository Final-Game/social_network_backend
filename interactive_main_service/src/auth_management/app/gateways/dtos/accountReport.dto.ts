export class AccountReportDto {
  receiverId: string;
  reason: string;

  constructor(receiverId: string, reason: string) {
    this.receiverId = receiverId;
    this.reason = reason;
  }
}
