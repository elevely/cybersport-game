from dataclasses import dataclass

from models.team import Team
from models.organization import Organization
from models.manager import Manager
from models.game_date import GameDate
from models.tournament import Tournament

from data.organizations import ORGANIZATIONS
from data.tournaments import TOURNAMENTS

@dataclass
class World:
    manager: Manager
    organization: Organization

    organizations: list[Organization]
    tournaments: list[Tournament]

    date: GameDate

    def advance_day(self):
        self.date.advance_day()

        self.report_day()

        self.process_daiy_events()
    
    def process_daiy_events(self):
        pass

    def report_day(self):
        print('==== Отчет за день ====')
        print('Сегодня событий не произошло')

    def flag_tournament(self):
        today_date = self.date.day + self.date.month * 30 + self.date.year * 365
        flag = False
        today_tournament = []

        for tournament in self.tournaments:
            tournament_date = tournament.start_day + tournament.start_month * 30 + tournament.start_year * 365
            if today_date == tournament_date:
                flag = True
                today_tournament = tournament
        
        if flag == True:
            return True, today_tournament
        else:
            return False, []

    def next_tournament(self):
        today_date = self.date.day + self.date.month * 30 + self.date.year * 365
        upcoming_tournaments = []

        for tournament in self.tournaments:
            tournament_date = tournament.start_day + tournament.start_month * 30 + tournament.start_year * 365
            if today_date < tournament_date:
                upcoming_tournaments.append(tournament)
        
        upcoming_tournaments.sort(
            key=lambda t:
                t.start_day +
                t.start_month * 30 +
                t.start_year * 365
            )

        if not upcoming_tournaments:
            print('В этом сезоне турниры закончились.')

        else:
            print('==== Ближайшие турниры ====')
            for tournament in upcoming_tournaments[:3]:
                print(f'Название: {tournament.name}')
                print(f'Призовой: {tournament.prize_pool}')
                print(f'Дата: {tournament.start_day}.{tournament.start_month}.{tournament.start_year}')
                print('')