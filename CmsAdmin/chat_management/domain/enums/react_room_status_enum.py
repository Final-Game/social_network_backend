from core.common.base_enum import BaseEnum


class ReactRoomStatusEnum(BaseEnum):
    HATE: int = 0
    LOVE: int = 1

    def __str__(self) -> str:
        if self.value == self.HATE:
            return "HATE"
        elif self.value == self.LOVE:
            return "LOVE"

        return super().__str__()

    def __int__(self):
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return ((int(cls.HATE), str(cls.HATE)), (int(cls.LOVE), str(cls.LOVE)))
