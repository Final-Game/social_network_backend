export class MediaDto {
  url: string;
  type: number;

  constructor(url: string, type: number) {
    this.url = url;
    this.type = type;
  }
}
