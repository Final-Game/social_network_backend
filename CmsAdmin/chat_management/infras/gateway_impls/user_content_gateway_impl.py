from chat_management.app.dtos.account_info_dto import AccountInfoDto
from chat_management.app.gateways import UserContentGateway


class UserContentGatewayImpl(UserContentGateway):
    def get_account_info(self, account_id: str) -> AccountInfoDto:
        from user_content.models import Account

        account: Account = Account.objects.find_account_by_id(account_id, False)

        return account and AccountInfoDto(account.id) or None