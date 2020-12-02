from core.app.bus import Query, QueryHandler
from user_content.models import Account, Profile


class GetAccountProfileQuery(Query):
    account_id: str

    def __init__(self, account_id: str) -> None:
        self.account_id = account_id

    def handler(self):
        return GetAccountProfileQueryHandler


class GetAccountProfileQueryHandler(QueryHandler):
    def handle(self, query: GetAccountProfileQuery) -> Account:
        account: Account = Account.objects.find_account_by_id(
            account_id=query.account_id, raise_exception=True
        )

        return account.profile