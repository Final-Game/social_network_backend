from abc import ABC
from typing import List
from user_content.app.dtos.user_create_post_dto import MediaPostData


class MediaService(ABC):
    def create_post_medias(self, post_id: str, media_datas: List[MediaPostData] = []):
        raise NotImplementedError()