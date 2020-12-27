export interface IUserMatchPayload {
  receiverId: string;
  status: number;
}

export interface ICreateMatchPayload {
  senderId: string;
  dto: IUserMatchPayload;
}
