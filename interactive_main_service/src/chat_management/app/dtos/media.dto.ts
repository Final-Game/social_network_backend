export class MediaDto {
  public url: string;
  public type: number;

  constructor(url: string, type: number) {
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
