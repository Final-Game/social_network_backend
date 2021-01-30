from abc import ABC
from chat_management.app.dtos.account_info_dto import AccountInfoDto


class UserContentGateway(ABC):
    def get_account_info(self, account_id: str) -> AccountInfoDto:
        raise NotImplementedError()