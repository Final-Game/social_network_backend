import { AbstractProjection } from 'node-cqrs';

/**
 * Users projection listens to events and updates associated view (read model)
 *
 * @class UsersProjection
 * @extends {AbstractProjection}
 */
class UserProjection extends AbstractProjection {
  /**
   * Events being handled by Projection
   * @type {string[]}
   * @readonly
   * @static
   * @memberof UsersProjection
   */
  static get handles() {
    return ['testEvent', 'userCreated'];
  }

  // async testEvent(event) {
  //   const { aggregateId, payload } = event;

  //   console.log('Test event handler');
  //   await this.view.create(aggregateId, {
  //     test: 'abc',
  //   });
  // }
}
export default UserProjection;
