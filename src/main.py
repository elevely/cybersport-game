from models.player import Player
from models.coach import Coach
from models.team import Team
from models.match import Match
from models.world import World
from models.tournament import Tournament

from services.match_simulator import MatchSimulator
from services.world_sumulator import WorldSimulator
from services.team_factory import create_test_team
from services.tournament_simulator import TournamentSimulator

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

tournament = Tournament(
    name="IEM Katowice",
    prize_pool=1000000,
    teams=teams[:8]
)

TournamentSimulator.play(tournament)