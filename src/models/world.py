from dataclasses import dataclass
from models.team import Team
from models.organization import Organization
from models.manager import Manager
from models.game_date import GameDate

@dataclass
class World:
    manager: Manager
    organization: Organization
    teams: list[Team]
    date: GameDate

    def advance_day(self):
        self.date.advance_day()

        self.process_daiy_events()
    
    def process_daiy_events(self):
        pass