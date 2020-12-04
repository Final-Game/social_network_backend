from core.common.base_enum import BaseEnum


class ModelStatusEnum(BaseEnum):
    ACTIVE: int = 1
    DISABLED: int = 0

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return ((int(cls.ACTIVE), "Active"), (int(cls.DISABLED), "Disabled"))
