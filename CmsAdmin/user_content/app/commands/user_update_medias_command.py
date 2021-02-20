from core.common.base_enum import BaseEnum
from user_content.domain.models.collection import Collection, MediaMapper
from core.common.base_api_exception import BaseApiException
from typing import List
from user_content.domain.models.profile import Profile
from user_content.domain.models.account import Account
from user_content.app.dtos.media_data_dto import MediaDataDto
from core.app.bus import Command, CommandHandler
from django.db import transaction


class UserUpdateMediasCommand(Command):
    account_id: str
    medias: List[MediaDataDto]

    def __init__(self, account_id: str, medias: List[MediaDataDto]) -> None:
        self.account_id = account_id
        self.medias = medias


class UserUpdateMediasCommandHandler(CommandHandler):
    def handle(self, command: UserUpdateMediasCommand):
        account: Account = Account.objects.find_account_by_id(command.account_id)
        account_profile: Profile = account.profile

        if not account_profile:
            raise BaseApiException("Please update account profile.")

        with transaction.atomic():
            collection: Collection = (
                getattr(account_profile, "collection", None)
                or account_profile.create_collection()
            )

            collection.update_medias(
                list(
                    map(
                        lambda x: MediaMapper(x.url, map_from_media_type(x.type)),
                        command.medias,
                    )
                )
            )

        return super().handle(command)


class MediaTypeDto(BaseEnum):
    VIDEO: int = 1
    PHOTO: int = 0


def map_from_media_type(media_type: str) -> int:
    if media_type == MediaTypeDto.PHOTO.name:
        return MediaTypeDto.PHOTO.value
    elif media_type == MediaTypeDto.VIDEO.name:
        return MediaTypeDto.VIDEO.value
