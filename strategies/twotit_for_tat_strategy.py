from include.player import Player
from strategies.strategy import Strategy


class TwoTitForTatStrategy(Strategy):

    def __init__(self, player: Player):
        self.player = player
        self.scores = []
        self.avg_score = 0

    def play(self) -> None:
        if len(self.player.plays) == 0:
            self.player.play(False)
            return
        if self.player.opposing_plays[-1] is True or (
            len(self.player.plays) > 1 and self.player.opposing_plays[-2] is True
        ):
            self.player.play(True)
            return
        self.player.play(False)

    def get_final_score(self, points: int) -> None:
        self.scores.append(points)

    def get_average_scores(self) -> None:
        self.avg_score = sum(self.scores) / len(self.scores)

    def __str__(self) -> str:
        super().__str__()
        return "Two Tit for tat"