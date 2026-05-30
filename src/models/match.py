from dataclasses import dataclass
from models.team import Team


@dataclass
class Match:
    team_a: Team
    team_b: Team