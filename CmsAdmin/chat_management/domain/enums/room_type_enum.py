from core.common.base_enum import BaseEnum


class RoomTypeEnum(BaseEnum):
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

        return super().__str__()

    def __int__(self):
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.NORMAL), str(cls.NORMAL)),
            (int(cls.SMART), str(cls.SMART)),
            (int(cls.MATCH), str(cls.MATCH)),
        )
