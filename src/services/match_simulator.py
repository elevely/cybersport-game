import random

from models.match import Match


class MatchSimulator:

    @staticmethod
    def simulate(match: Match):

        power_a = match.team_a.get_strength()
        power_b = match.team_b.get_strength()

        form_a = random.uniform(-5, 5)
        form_b = random.uniform(-5, 5)

        power_a += form_a
        power_b += form_b   

        win_chance = power_a / (power_a + power_b)

        if random.random() < win_chance:
            return (match.team_a, match.team_b)

        return (match.team_b, match.team_a)