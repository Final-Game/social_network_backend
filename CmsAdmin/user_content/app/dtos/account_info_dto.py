from datetime import date
from dataclasses import dataclass


@dataclass
class AccountInfoDto:
    id: str
    full_name: str
    avatar: str
    birth_date: date
    gender: int