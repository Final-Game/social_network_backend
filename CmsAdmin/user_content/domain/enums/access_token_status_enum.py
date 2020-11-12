from core.common.base_enum import BaseEnum


class AccessTokenStatusEnum(BaseEnum):
    ACTIVE = 0
    IN_ACTIVE = 1
    BLACK_LIST = 2

    def __int__(self):
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.ACTIVE), "ACTIVE"),
            (int(cls.IN_ACTIVE), "IN_ACTIVE"),
            (int(cls.BLACK_LIST), "BLACK_LIST"),
        )
