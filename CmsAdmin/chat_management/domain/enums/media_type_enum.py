from core.common.base_enum import BaseEnum


class MediaTypeEnum(BaseEnum):
    VIDEO: int = 0
    PHOTO: int = 1

    def __str__(self) -> str:
        if self.value == self.VIDEO:
            return "VIDEO"
        elif self.value == self.PHOTO:
            return "PHOTO"
        return super().__str__()

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls) -> tuple:
        return ((int(cls.VIDEO), str(cls.VIDEO)), (int(cls.PHOTO), str(cls.PHOTO)))
