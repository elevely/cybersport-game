from dataclasses import dataclass
from models.team import Team

@dataclass
class Tournament:
    name: str
    prize_pool: int
    teams: list[Team]