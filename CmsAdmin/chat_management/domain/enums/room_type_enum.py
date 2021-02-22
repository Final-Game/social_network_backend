from core.common.base_enum import BaseEnum


class RoomTypeEnum(BaseEnum):
    SMART_PENDING: int = -1
    NORMAL: int = 0
    SMART: int = 1
    MATCH: int = 2

    def __str__(self) -> str:
        if self.value == self.NORMAL:
            return "NORMAL"
        elif self.value == self.SMART:
            return "SMART"
        elif self.value == self.MATCH:
            return "MATCH"
        elif self.value == self.SMART_PENDING:
            return "SMART_PENDING"

        return super().__str__()

    def __int__(self):
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.NORMAL), str(cls.NORMAL)),
            (int(cls.SMART), str(cls.SMART)),
            (int(cls.MATCH), str(cls.MATCH)),
            (int(cls.SMART_PENDING), str(cls.SMART_PENDING)),
        )
