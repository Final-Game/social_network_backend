from media_content.app.dtos.create_media_list_dto import CreatePostMediaListDto
from media_content.app.commands.create_post_medias_command import (
    CreatePostMediasCommand,
)
from media_content.app.dtos.media_dto import MediaDto
from typing import List

from core.app.bus import Bus

from user_content.app.dtos.user_create_post_dto import MediaPostData
from user_content.app.services import MediaService


class MediaServiceImpl(MediaService):
    __bus: Bus

    def __init__(self, bus: Bus = Bus()) -> None:
        self.__bus = bus

    def create_post_medias(self, post_id: str, media_datas: List[MediaPostData]):

        self.__bus.dispatch(
            CreatePostMediasCommand(
                CreatePostMediaListDto(
                    post_id, list(map(lambda x: map_media_data_to_dto(x), media_datas))
                )
            )
        )
        

def map_media_data_to_dto(media_post_data: MediaPostData):
    return MediaDto(media_post_data.url, media_post_data.type)
