from include.player import Player
from strategies.strategy import Strategy


class TitForTatStrategy(Strategy):

    def __init__(self, player: Player):
        self.player = player

    def play(self) -> None:
        if len(self.player.plays) == 0:
            self.player.play(False)
            return
        if self.player.plays[-1] is True:
            self.player.play(True)
            return
        self.player.play(False)
        return

    def __str__(self) -> str:
        super().__str__()
        return "Tit for tat"
