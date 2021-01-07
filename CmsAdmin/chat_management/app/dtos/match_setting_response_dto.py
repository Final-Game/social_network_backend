from dataclasses import dataclass


@dataclass
class MatchSettingResponseDto:
    min_age: int
    max_age: int
    max_distance: float
    target_gender: str