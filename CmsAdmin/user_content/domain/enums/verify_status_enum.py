from core.common.base_enum import BaseEnum


class VerifyStatusEnum(BaseEnum):
    PENDING: int = 0
    VERIFIED: int = 1
    REJECTED: int = -1

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (cls.PENDING.value, cls.PENDING.name),
            (cls.VERIFIED.value, cls.VERIFIED.name),
            (cls.REJECTED.value, cls.REJECTED.name),
        )