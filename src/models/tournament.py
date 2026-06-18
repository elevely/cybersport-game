from dataclasses import dataclass
from models.organization import Organization

@dataclass
class Tournament:
    name: str
    prize_pool: int
    start_day: int
    start_month: int
    start_year: int
    organizations: list[Organization]