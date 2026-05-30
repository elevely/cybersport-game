from dataclasses import dataclass
from models.team import Team
from models.organization import Organization
from models.manager import Manager

@dataclass
class World:
    manager: Manager
    organization: Organization
    teams: list[Team]

    current_day: int = 1
    current_month: int = 1
    current_year: int = 2026