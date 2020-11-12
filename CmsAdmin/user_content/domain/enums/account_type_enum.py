from core.common.base_enum import BaseEnum


class AccountTypeEnum(BaseEnum):
    NORMAL: int = 0
    ADMIN: int = 1
    SYS_ADMIN: int = 2

    def __str__(self) -> str:
        if self.value == self.NORMAL:
            return "NORMAL"
        elif self.value == self.ADMIN:
            return "ADMIN"
        elif self.value == self.SYS_ADMIN:
            return "SYS_ADMIN"

    def __int__(self):
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.NORMAL), str(cls.NORMAL)),
            (int(cls.ADMIN), str(cls.ADMIN)),
            (int(cls.SYS_ADMIN), str(cls.SYS_ADMIN)),
        )