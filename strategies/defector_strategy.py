from include.player import Player
from strategies.strategy import Strategy


class DefectorStrategy(Strategy):

    def __init__(self, player: Player):
        self.player = player

    def play(self) -> None:
        self.player.play(True)

    def __str__(self) -> str:
        return "Unconditional defector"
