import { matchHandlers } from './match.msg_handler';

let chatHandlers = [];

chatHandlers = chatHandlers.concat(matchHandlers);

export { chatHandlers };
