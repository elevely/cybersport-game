from dataclasses import dataclass


@dataclass
class Player:
    name: str
    nick: str
    age: int
    salary: int
    general_aim: int
    pistol_aim: int
    macro_mechanics: int
    micro_mechanics: int
    stability: int
    stress_resistance: int
    media: int
    friendly_lvl: int