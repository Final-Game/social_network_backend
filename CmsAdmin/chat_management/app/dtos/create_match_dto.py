from dataclasses import dataclass


@dataclass
class CreateMatchDto:
    receiver_id: str
    status: int
