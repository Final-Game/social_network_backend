import { getConnection } from 'typeorm';
import BaseException from '../exceptions/BaseException';

export interface IBaseRepository {
  save: (entity: any) => Promise<any>;
  update: (entityId: string, data: any) => Promise<void>;
  findById: (entityId: string, raiseException: boolean) => Promise<any>;
}

export class BaseRepository implements IBaseRepository {
  protected model: any;

  public async save(entity: any): Promise<any> {
    const manager = getConnection().manager;

    return await manager.save(this.model, entity);
  }

  public async update(entityId: string, data: any): Promise<void> {
    const manager = getConnection().manager;

    await manager.update(this.model, entityId, data);
  }

  public async findById(entityId: string, raiseException: boolean): Promise<any> {
    const manager = getConnection().manager;

    const entity: any = await manager.findOne(this.model, { where: { id: entityId } });

    if (!entity && raiseException) {
      throw new BaseException(`Can't find entity with id: ${entityId}`);
    }

    return entity;
  }
}
