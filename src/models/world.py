from dataclasses import dataclass
from models.team import Team

@dataclass
class World:
    teams: list[Team]
    current_day: int = 1
    current_month: int = 1
    current_year: int = 2026