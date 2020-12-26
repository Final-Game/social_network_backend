from core.common.base_enum import BaseEnum


class MatchStatusEnum(BaseEnum):
    CLOSE: int = 0
    LOVE: int = 1
    SUPER_LOVE: int = 2

    def __str__(self) -> str:
        if self.value == self.CLOSE:
            return "CLOSE"
        elif self.value == self.LOVE:
            return "LOVE"
        elif self.value == self.SUPER_LOVE:
            return "SUPER_LOVE"

        return super().__str__()

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.CLOSE), str(cls.CLOSE)),
            (int(cls.LOVE), str(cls.LOVE)),
            (int(cls.SUPER_LOVE), str(cls.SUPER_LOVE)),
        )