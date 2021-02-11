from dataclasses import dataclass


@dataclass
class MatcherDto:
    matcher_id: str
    name: str
    age: int
    bio: str
    status: int