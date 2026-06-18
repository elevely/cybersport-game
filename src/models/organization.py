from dataclasses import dataclass
from models.team import Team


@dataclass
class Organization:
    name: str
    money: int
    
    team: Team

    wins: int = 0
    losses: int = 0
