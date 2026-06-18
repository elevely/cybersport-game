from models.tournament import Tournament
from data.organizations import ORGANIZATIONS

TOURNAMENTS = [
    Tournament(
        name = 'IEM Katowice',
        prize_pool = 1000000,
        start_day = 15,
        start_month = 1,
        start_year = 2026,
        organizations=ORGANIZATIONS[:8]
    ),

    Tournament(
        name = 'ESL Pro League',
        prize_pool = 800000,
        start_day = 10,
        start_month = 2,
        start_year = 2026,
        organizations=ORGANIZATIONS[:8]

    ),

    Tournament(
        name = 'Blast Series',
        prize_pool = 1000000,
        start_day = 20,
        start_month = 3,
        start_year = 2026,
        organizations=ORGANIZATIONS[:8]
    )
]