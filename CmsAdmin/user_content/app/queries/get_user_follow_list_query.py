from core.common.pageable import Pageable
from typing import List
from user_content.domain.models.account import Account
from core.app.bus import Query, QueryHandler


class UserFollowMetadata(object):
    page: int
    limit: int

    def __init__(self, page: int = 0, limit: int = 50) -> None:
        self.page = page
        self.limit = limit


class GetUserFollowListQuery(Query):
    account_id: str
    metadata: UserFollowMetadata

    def __init__(
        self, account_id: str, metadata: UserFollowMetadata = UserFollowMetadata()
    ) -> None:
        self.account_id = account_id
        self.metadata = metadata


class GetUserFollowListQueryHandler(QueryHandler):
    def handle(self, query: GetUserFollowListQuery) -> List[Account]:
        account: Account = Account.objects.find_account_by_id(
            query.account_id, raise_exception=True
        )

        user_followes: List[Account] = Account.objects.query_user_follows_for_account(
            account, pageable=Pageable(query.metadata.page, query.metadata.limit)
        )
        return list(user_followes)