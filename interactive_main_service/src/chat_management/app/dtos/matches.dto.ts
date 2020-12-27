export class ReceiverMatchDto {
  public receiverId: string;
  public status: number;
}

export class CreateMatchDto {
  public accountId: string;
  public dto: ReceiverMatchDto;
}
