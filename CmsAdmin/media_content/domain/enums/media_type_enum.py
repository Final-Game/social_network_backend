from core.common.base_enum import BaseEnum


class MediaTypeEnum(BaseEnum):
    VIDEO: int = 1
    PHOTO: int = 0

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return ((int(cls.VIDEO), cls.VIDEO.name), (int(cls.PHOTO), cls.PHOTO.name))
