import { Entity, PrimaryGeneratedColumn, Column, Unique, CreateDateColumn, UpdateDateColumn, AfterInsert } from 'typeorm';
import { IsNotEmpty } from 'class-validator';
import { User } from '../models/users.model';

@Entity('uc_accounts')
export class UserEntity implements User {
  @PrimaryGeneratedColumn('uuid')
  id: string;

  @Column()
  @IsNotEmpty()
  username: string;

  @Column()
  @IsNotEmpty()
  password: string;

  @Column()
  type: number;

  @Column({ name: 'created_at' })
  // @CreateDateColumn()
  createdAt: Date;

  @Column({ name: 'updated_at' })
  // @UpdateDateColumn()
  updatedAt: Date;

  // @AfterInsert()
  // initializeDefault() {
  //   if (!this.type) {
  //     this.type = 0;
  //   }
  // }
}
