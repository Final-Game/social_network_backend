from typing import List
from .media_dto import MediaDto


class CreatePostMediaListDto:
    medias: List[MediaDto]
    post_id: str

    def __init__(self, post_id: str, medias: List[MediaDto]) -> None:
        self.post_id = post_id
        self.medias = medias
