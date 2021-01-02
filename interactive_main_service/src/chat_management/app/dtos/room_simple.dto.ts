import { Room } from '../../domain/models/rooms.model';

export class RoomSimpleDto {
  id: string;

  constructor(room: Room) {
    this.id = room.id;
  }
}
