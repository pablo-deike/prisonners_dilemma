from strategies.strategy import Strategy


class Player:

    def __init__(self):
        self.points = 0
        self.defects = False
        self.plays = []
        self.opposing_plays = []

    def add_points(self, points: int) -> None:
        self.points += points

    def play(self, defect: bool) -> None:
        self.defects = defect
        self.plays.append(self.defects)

    def add_opposing_plays(self, defect: bool) -> None:
        self.opposing_plays.append(defect)

    def reset_player(self) -> None:
        self.points = 0
        self.plays = []
        self.opposing_plays = []
