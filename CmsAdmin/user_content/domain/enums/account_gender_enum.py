from core.common.base_enum import BaseEnum


class AccountGenderEnum(BaseEnum):
    MALE: int = 0
    FAMALE: int = 1
    UN_KNOWN: int = 2

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.MALE), "Male"),
            (int(cls.FAMALE), "Female"),
            (int(cls.UN_KNOWN), "Unknown"),
        )

    @classmethod
    def to_dict(cls) -> dict:
        MALE = int(cls.MALE)
        FEMALE = int(cls.FAMALE)
        UN_KNOWN = int(cls.UN_KNOWN)

        return {MALE: "MALE", FEMALE: "FEMALE", UN_KNOWN: "UN_KNOWN"}
