from player.player import Player
from strategies.strategy import Strategy


class DefectorStrategy(Strategy):

    def __init__(self, player: Player):
        self.player = player
        self.scores = []
        self.avg_score = 0

    def play(self) -> None:
        self.player.play(True)

    def get_final_score(self, points: int) -> None:
        self.scores.append(points)

    def get_average_scores(self) -> None:
        self.avg_score = sum(self.scores) / len(self.scores)

    def __str__(self) -> str:
        return "Unconditional defector"
