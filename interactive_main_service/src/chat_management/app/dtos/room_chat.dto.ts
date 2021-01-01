export class RoomChatDto {
  id: string;
  avtIconUrl: string;
  name: string;
  latestMsg: string;
  latestMsgTime: Date;
  numUnReadMsg: number;

  constructor(id: string, avtIconUrl: string, name: string, numUnReadMsg: number, latestMsg: string, latestMsgTime: Date) {
    this.id = id;
    this.name = name;
    this.avtIconUrl = avtIconUrl;
    this.numUnReadMsg = numUnReadMsg;
    this.latestMsg = latestMsg;
    this.latestMsgTime = latestMsgTime;
  }

  public toResData(): any {
    return {
      id: this.id,
      avt_icon_url: this.avtIconUrl,
      name: this.name,
      latest_msg: this.latestMsg,
      latest_msg_time: this.latestMsgTime.toISOString(),
      num_un_read_msg: this.numUnReadMsg,
    };
  }
}
