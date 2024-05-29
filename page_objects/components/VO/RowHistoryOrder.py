from dataclasses import dataclass


@dataclass
class RowHistoryOrder:
    stage_start: str
    stage_ent: str
    stage_name: str
    detail: str | None
    result: str
    user_name: str
    reason: str | None
    comment: str | None
    appointed: str | None
    appointed_date: str | None
