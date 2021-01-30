import { EntityManager, getConnection } from 'typeorm';

class ConnectManager {
  private static _manager: EntityManager = null;
  private static _available = true;

  /**
   * set connection
   */
  public static setManager(manager: EntityManager) {
    if (this._available) {
      this._manager = manager;
      this._available = false;
    }
  }

  public static clearManager(manager: EntityManager) {
    if (this._manager === manager) {
      this._manager = null;
      this._available = true;
    }
  }

  public static getManager(): EntityManager {
    if (!this._available) {
      return this._manager;
    }
    return getConnection().manager;
  }
}

const RunInTransaction = async (task: (manager: EntityManager) => any) => {
  const connection = getConnection();

  const queryRunner = connection.createQueryRunner();

  await queryRunner.connect();
  await queryRunner.startTransaction();
  ConnectManager.setManager(queryRunner.manager);

  try {
    await task(queryRunner.manager);

    await queryRunner.commitTransaction();
  } catch (err) {
    await queryRunner.rollbackTransaction();
    throw err;
  } finally {
    ConnectManager.clearManager(queryRunner.manager);
    await queryRunner.release();
  }
};

export { RunInTransaction, ConnectManager };
