from core.common.base_enum import BaseEnum


class PostTypeEnum(BaseEnum):
    ACTIVE: int = 1
    HIDDEN: int = 0

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return ((int(cls.ACTIVE), cls.ACTIVE.name), (int(cls.HIDDEN), cls.HIDDEN.name))
