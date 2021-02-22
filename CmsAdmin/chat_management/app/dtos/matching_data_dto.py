from chat_management.app.dtos.matcher_data_dto import MatcherDataDto
from dataclasses import dataclass
from typing import List


@dataclass
class MatchingDataDto:
    num_smart_chat_users: int
    num_traditional_match_users: int
    nearly_users: List[MatcherDataDto]