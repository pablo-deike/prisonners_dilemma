from include.player import Player
from strategies.strategy import Strategy


class CooperatorStrategy(Strategy):

    def __init__(self, player: Player):
        self.player = player

    def play(self) -> None:
        self.player.play(False)

    def __str__(self) -> str:
        return "Unconditional cooperator"
