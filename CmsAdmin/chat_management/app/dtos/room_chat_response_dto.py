from dataclasses import dataclass
from datetime import datetime


@dataclass
class RoomChatResponseDto:
    id: str
    avt_icon_url: str
    name: str
    latest_msg: str
    latest_msg_time: datetime
    num_un_read_msg: int
    type: int = 0