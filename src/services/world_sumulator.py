import random

from models.match import Match
from services.match_simulator import MatchSimulator


class WorldSimulator:

    @staticmethod
    def simulate_day(world):

        if len(world.teams) < 2:
            return

        random.shuffle(world.teams)
        
        print(f'{world.current_day}.{world.current_month}.{world.current_year}')

        for i in range(0, len(world.teams), 2):

            team_a = world.teams[i]
            team_b = world.teams[i + 1]

            match = Match(team_a, team_b)

            winner = MatchSimulator.simulate(match)

            if winner == team_a:
                team_a.wins += 1
                team_b.losses += 1
            else:
                team_b.wins += 1
                team_a.losses += 1

            print(f"{team_a.name} vs {team_b.name}")
            print(f"Winner: {winner.name}")

        sorted_teams = sorted(
            world.teams,
            key=lambda team: team.wins,
            reverse=True
        )

        world.current_day += 1

        if world.current_day == 32:
            world.current_day = 1
            world.current_month += 1
    
        if world.current_month == 13:
            world.current_month = 1
            world.current_year += 1

    @staticmethod
    def simulate_week(world):
        for _ in range(7):
            WorldSimulator.simulate_day(world)
