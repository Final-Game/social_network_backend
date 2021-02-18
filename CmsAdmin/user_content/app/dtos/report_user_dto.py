from dataclasses import dataclass


@dataclass
class ReportUserDto:
    receiver_id: str
    reason: str
    related_post_id: str = ""