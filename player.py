from strategies.strategy import Strategy


class Player:

    def __init__(self, strategy: Strategy):
        self.points = 0
        self.conflict = False
        self.strategy = strategy
        self.plays = []

    def add_points(self, points: int) -> None:
        self.points += points

    def play(self, plays: list) -> None:
        if len(self.plays) == 0:
            self.plays.append(self.conflict)
            return
        self.conflict = self.strategy.play(last_plays=plays)
        self.plays.append(self.conflict)
