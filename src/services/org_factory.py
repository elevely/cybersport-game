from models.player import Player
from models.coach import Coach
from models.team import Team
from models.organization import Organization
import random

def create_test_org(name: str) -> Organization:
    return Organization(
        name=name,
        money=100000,

        team = Team(
        players=[
            Player("Player1", "P1", random.randint(18, 27), 5000, random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), 50, random.randint(78, 96)),
            Player("Player2", "P2", random.randint(18, 27), 5000, random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), 50, random.randint(78, 96)),
            Player("Player3", "P3", random.randint(18, 27), 5000, random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), 50, random.randint(78, 96)),
            Player("Player4", "P4", random.randint(18, 27), 5000, random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), 50, random.randint(78, 96)),
            Player("Player5", "P5", random.randint(18, 27), 5000, random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), random.randint(78, 96), 50, random.randint(78, 96)),
        ],
        coach=Coach(
            "Coach",
            "Coach",
            35,
            5000,
            random.randint(78, 96),
            random.randint(78, 96),
            random.randint(78, 96)
        ),
        )
    )