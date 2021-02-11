from dataclasses import dataclass


@dataclass
class MatcherInfoDto:
    matcher_id: str
    name: str
    age: int
    gender: int
    address: str
    job: str
    reason: str