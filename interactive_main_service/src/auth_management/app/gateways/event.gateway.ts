export interface EventGateway {
  matchUser(accountId: string, partnerId: string): Promise<void>;
}
