from core.common.base_enum import BaseEnum


class AccountGenderEnum(BaseEnum):
    MALE: int = 0
    FEMALE: int = 1
    UN_KNOWN: int = 2

    def __int__(self) -> int:
        return int(self.value)

    @classmethod
    def to_choices(cls):
        return (
            (int(cls.MALE), "Male"),
            (int(cls.FEMALE), "Female"),
            (int(cls.UN_KNOWN), "Unknown"),
        )

    @classmethod
    def to_dict(cls) -> dict:
        MALE = int(cls.MALE)
        FEMALE = int(cls.FEMALE)
        UN_KNOWN = int(cls.UN_KNOWN)

        return {MALE: "MALE", FEMALE: "FEMALE", UN_KNOWN: "UN_KNOWN"}

    @classmethod
    def from_value(cls, val_str: str):
        if val_str == "MALE":
            return int(cls.MALE)
        elif val_str == "FEMALE":
            return int(cls.FEMALE)
        elif val_str == "UN_KNOWN":
            return int(cls.UN_KNOWN)
        else:
            return None
