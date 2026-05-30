from models.player import Player
from models.coach import Coach
from models.team import Team


def create_test_team(name: str) -> Team:
    return Team(
        name=name,
        players=[
            Player("Player1", "P1", 22, 5000, 80, 80, 80, 80, 80, 80, 50, 80),
            Player("Player2", "P2", 22, 5000, 80, 80, 80, 80, 80, 80, 50, 80),
            Player("Player3", "P3", 22, 5000, 80, 80, 80, 80, 80, 80, 50, 80),
            Player("Player4", "P4", 22, 5000, 80, 80, 80, 80, 80, 80, 50, 80),
            Player("Player5", "P5", 22, 5000, 80, 80, 80, 80, 80, 80, 50, 80),
        ],
        coach=Coach(
            "Coach",
            "Coach",
            35,
            5000,
            80,
            80,
            80
        ),
        money=100000
    )