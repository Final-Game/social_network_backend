from typing import Tuple
from core.common.base_enum import BaseEnum


class AccountReportStatusEnum(BaseEnum):
    RESOLVED: int = 1
    UN_RESOLVED: int = 0

    def __int__(self):
        return self.value

    @classmethod
    def to_choices(cls) -> tuple:
        return (
            (cls.RESOLVED.value, cls.RESOLVED.name),
            (cls.UN_RESOLVED.value, cls.UN_RESOLVED.name),
        )