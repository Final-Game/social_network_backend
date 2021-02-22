from dataclasses import dataclass


@dataclass
class MatcherDataDto:
    id: str
    avatar: str
    name: str
    bio: str
    age: int
    gender: int