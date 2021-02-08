from core.common.base_enum import BaseEnum


class AccountStatusEnum(BaseEnum):
    ACTIVE: int = 1
    DEACTIVE: int = 0
    BANNED: int = 2

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (cls.ACTIVE.value, cls.ACTIVE.name),
            (cls.DEACTIVE.value, cls.DEACTIVE.name),
            (cls.BANNED.value, cls.BANNED.name),
        )