from core.common.base_enum import BaseEnum


class ReactTypeEnum(BaseEnum):
    LIKE: int = 0
    LOVE: int = 1

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return ((int(cls.LIKE), "Like"), (int(cls.LOVE), "Love"))

    @classmethod
    def to_dict(cls) -> dict:
        return {int(cls.LIKE): "Like", int(cls.LOVE): "Love"}

    @classmethod
    def from_value(cls, val_str: str):
        if val_str == "LIKE":
            return int(cls.LIKE)
        elif val_str == "LOVE":
            return int(cls.LOVE)
        else:
            return None

    @classmethod
    def to_value(cls, val_int: int):
        if val_int == cls.LIKE:
            return "LIKE"
        elif val_int == cls.LOVE:
            return "LOVE"
        else:
            return None
