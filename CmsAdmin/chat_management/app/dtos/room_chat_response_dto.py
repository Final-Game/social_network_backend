from dataclasses import dataclass


@dataclass
class RoomChatResponseDto:
    id: str
    avt_icon_url: str
    name: str
    latest_msg: str
    latest_msg_time: str
    num_un_read_msg: int