from core.common.base_enum import BaseEnum


class MediaTypeDto(BaseEnum):
    VIDEO: int = 1
    PHOTO: int = 0


def map_media_type(media_type: int) -> str:
    if media_type == MediaTypeDto.PHOTO:
        return MediaTypeDto.PHOTO.name
    elif media_type == MediaTypeDto.VIDEO:
        return MediaTypeDto.VIDEO.name
