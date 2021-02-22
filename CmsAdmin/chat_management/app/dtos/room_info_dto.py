from dataclasses import dataclass


@dataclass
class RoomInfoDto:
    id: str
    partner_id: str
    partner_name: str