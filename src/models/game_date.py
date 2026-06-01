from dataclasses import dataclass

@dataclass
class GameDate:
    day: int
    month: int
    year: int

    def advance_day(self):
        self.day += 1

        if self.day > 30:
            self.day = 1
            self.month += 1
            
        if self.month > 12:
            self.month = 1
            self.year += 1