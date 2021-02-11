import { BaseEntity, BeforeInsert, BeforeUpdate, Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';

export class GenericEntity extends BaseEntity {
  @Column({ name: 'created_at' })
  createdAt: Date;

  @Column({ name: 'updated_at' })
  updatedAt: Date;

  protected triggerUpdate() {
    this.updatedAt = new Date();
  }

  protected triggerCreate() {
    this.createdAt = new Date();
    this.updatedAt = new Date();
  }
}
