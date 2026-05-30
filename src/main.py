from models.player import Player
from models.coach import Coach
from models.team import Team
from models.match import Match
from models.world import World

from services.match_simulator import MatchSimulator
from services.world_sumulator import WorldSimulator
from services.team_factory import create_test_team

team_names = [
    "NAVI",
    "Spirit",
    "Vitality",
    "G2",
    "FaZe",
    "MOUZ",
    "Astralis",
    "Falcons",
    "Liquid",
    "The MongolZ"
]

teams = [
    create_test_team(name)
    for name in team_names
]

world = World(teams)

WorldSimulator.simulate_week(world)

print("\nTABLE")

for team in world.teams:
    print(
        f"{team.name} | "
        f"W:{team.wins} "
        f"L:{team.losses}"
    )