from datetime import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class MediaChatDto:
    url: str
    type: int


@dataclass
class MessageChatReponseDto:
    id: str
    sender_id: str
    content: str
    created_at: datetime
    media_data: List[MediaChatDto] = []