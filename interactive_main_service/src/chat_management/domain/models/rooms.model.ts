export interface Room {
  id: string;
  generalName: string;
  type: number;
  createdAt: Date;
  updatedAt: Date;

  getMemberIds: () => Promise<Array<any>>;
}
