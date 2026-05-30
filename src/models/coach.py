from dataclasses import dataclass


@dataclass
class Coach:
    name: str
    nick: str
    age: int
    salary: int
    macro_mechanics: int
    stability: int
    friendly_lvl: int