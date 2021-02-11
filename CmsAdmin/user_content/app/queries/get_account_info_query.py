from user_content.app.dtos.account_info_dto import AccountInfoDto
from core.app.bus import Query, QueryHandler
from user_content.models import Account, Profile


class GetAccountInfoQuery(Query):
    account_id: str

    def __init__(self, account_id: str) -> None:
        self.account_id = account_id


class GetAccountInfoQueryHandler(QueryHandler):
    def handle(self, query: GetAccountInfoQuery) -> AccountInfoDto:
        account: Account = Account.objects.find_account_by_id(
            account_id=query.account_id, raise_exception=True
        )

        account_profile: Profile = account.profile

        return AccountInfoDto(
            account.id,
            account_profile and account_profile.full_name,
            account_profile and account_profile.avatar,
            account_profile and account_profile.birth_date,
            account_profile and account_profile.gender,
            account_profile and account_profile.bio,
            account_profile and account_profile.address,
            account_profile and account_profile.school,
            account_profile and account_profile.reason_dating,
        )
