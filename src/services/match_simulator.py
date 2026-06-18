import random

from models.match import Match


class MatchSimulator:

    @staticmethod
    def simulate(match: Match):

        power_a = match.organization_a.team.get_strength()
        power_b = match.organization_b.team.get_strength()

        form_a = random.uniform(-5, 5)
        form_b = random.uniform(-5, 5)

        power_a += form_a
        power_b += form_b   

        win_chance = power_a / (power_a + power_b)

        if random.random() < win_chance:
            return (match.organization_a, match.organization_b)

        return (match.organization_a, match.organization_b)