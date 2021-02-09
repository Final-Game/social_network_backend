import { Message } from '../../domain/models/message.model';

export class MediaMessageDto {
  url: string;
  type: string;

  constructor(url: string, type: string) {
    this.url = url;
    this.type = type;
  }

  public toResData(): any {
    return {
      url: this.url,
      type: this.type,
    };
  }
}

export class MessageDto {
  id: string;
  senderId: string;
  content: string;
  mediaData: Array<MediaMessageDto>;
  createdAt: Date;

  constructor(message: Message, accountId: string, mediaData: Array<MediaMessageDto> = null) {
    this.id = message.id;
    this.senderId = accountId;
    this.content = message.content;
    this.mediaData = mediaData;
    this.createdAt = message.createdAt;
  }

  public toResData(): any {
    return {
      id: this.id,
      sender_id: this.senderId,
      content: this.content,
      media_data: this.mediaData.map(item => item.toResData()),
      created_at: this.createdAt.toISOString(),
    };
  }
}

// string id = 1;
// string sender_id = 2;
// string content = 3;
// repeated MediaChat media_data = 4;
// string created_at = 5;
