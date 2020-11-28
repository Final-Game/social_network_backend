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
