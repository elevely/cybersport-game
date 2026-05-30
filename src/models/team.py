from dataclasses import dataclass
from models.player import Player
from models.coach import Coach


@dataclass
class Team:
    name: str
    players: list[Player]
    coach: Coach
    money: int
    wins: int = 0
    losses: int = 0

    def get_strength(self) -> float:
        avg_general_aim = sum(player.general_aim for player in self.players) / len(self.players)
        avg_pistol_aim = sum(player.pistol_aim for player in self.players) / len(self.players)
        avg_macro_mechanics = sum(player.macro_mechanics for player in self.players) / len(self.players)
        avg_micro_mechanics = sum(player.micro_mechanics for player in self.players) / len(self.players)
        avg_stability = sum(player.stability for player in self.players) / len(self.players)
        avg_stress_resistance = sum(player.stress_resistance for player in self.players) / len(self.players)
        avg_friendly_lvl = sum(player.friendly_lvl for player in self.players) / len(self.players)

        avg_rating = avg_general_aim * 0.3 + avg_pistol_aim * 0.05 + avg_macro_mechanics * 0.35 + \
            avg_micro_mechanics * 0.15 + avg_stability * 0.05 + avg_stress_resistance * 0.05 + avg_friendly_lvl * 0.05

        coach_bonus = (self.coach.macro_mechanics * 0.05 + self.coach.stability * 0.05 + self.coach.friendly_lvl * 0.05) / 60

        return avg_rating + coach_bonus