export class RoomInfoDto {
  id: string;
  partnerId: string;
  partnerName: string;

  constructor(id: string, partnerId: string, partnerName: string) {
    this.id = id;
    this.partnerId = partnerId;
    this.partnerName = partnerName;
  }

  public toResData(): any {
    return {
      id: this.id,
      partner_id: this.partnerId,
      partner_name: this.partnerName,
    };
  }
}
