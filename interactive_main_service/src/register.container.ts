import registerAuthDI from "./auth_management/domain/di.registers";
import container from "./container";

function registerContainer() {
  registerAuthDI();
  container.createUnexposedInstances();
}


export default registerContainer;
