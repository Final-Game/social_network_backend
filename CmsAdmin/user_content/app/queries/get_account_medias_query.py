from typing import List
from user_content.app.dtos.media_data_dto import MediaDataDto
from user_content.domain.models.profile import Profile
from user_content.domain.models.collection import Collection
from core.app.bus import Query, QueryHandler
from user_content.models import Account
from core.common.base_enum import BaseEnum


class GetAccountMediasQuery(Query):
    account_id: str

    def __init__(self, account_id: str) -> None:
        self.account_id = account_id


class GetAccountMediasQueryHandler(QueryHandler):
    def handle(self, query: GetAccountMediasQuery) -> List[MediaDataDto]:
        account: Account = Account.objects.find_account_by_id(
            query.account_id, raise_exception=True
        )
        account_profile: Profile = account.profile
        collection: Collection = account_profile and getattr(
            account_profile, "collection", None
        )
        return (
            collection
            and list(
                map(
                    lambda x: MediaDataDto(x.url, map_media_type(x.type)),
                    collection.medias.all(),
                )
            )
            or []
        )


class MediaTypeDto(BaseEnum):
    VIDEO: int = 1
    PHOTO: int = 0


def map_media_type(media_type: int) -> str:
    if media_type == MediaTypeDto.PHOTO:
        return MediaTypeDto.PHOTO.name
    elif media_type == MediaTypeDto.VIDEO:
        return MediaTypeDto.VIDEO.name
