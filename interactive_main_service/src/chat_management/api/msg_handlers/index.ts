import { chatHandlers } from './chat.msg_handlers';
import { matchHandlers } from './match.msg_handler';

let chatModuleHandler = [];

chatModuleHandler = chatModuleHandler.concat(matchHandlers).concat(chatHandlers);

export { chatModuleHandler };
