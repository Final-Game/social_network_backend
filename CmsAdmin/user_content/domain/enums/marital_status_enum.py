from core.common.base_enum import BaseEnum


class MaritalStatusEnum(BaseEnum):
    SINGLE: int = 0
    MARRIED: int = 1

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return ((int(cls.SINGLE), "Single"), (int(cls.MARRIED), "Married"))

    @classmethod
    def to_dict(cls) -> dict:
        return {int(cls.SINGLE): "SINGLE", int(cls.MARRIED): "MARRIED"}

    @classmethod
    def from_value(cls, val_str: str):
        if val_str == "SINGLE":
            return int(cls.SINGLE)
        elif val_str == "MARRIED":
            return int(cls.MARRIED)
        else:
            return None

    @classmethod
    def to_value(cls, val_int: int):
        if val_int == cls.SINGLE:
            return "SINGLE"
        elif val_int == cls.MARRIED:
            return "MARRIED"
        else:
            return None