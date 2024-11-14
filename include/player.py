from strategies.strategy import Strategy


class Player:

    def __init__(self):
        self.points = 0
        self.defects = False
        self.plays = []

    def add_points(self, points: int) -> None:
        self.points += points

    def play(self, defect: bool) -> None:
        self.defects = defect
        self.plays.append(self.defects)
