import random

from include.player import Player
from strategies.strategy import Strategy


class RandomStrategy(Strategy):

    def __init__(self, player: Player):
        self.player = player

    def play(self) -> bool:
        return self.player.play(random.uniform(0, 1) <= 0.5)

    def __str__(self) -> str:
        super().__str__()
        return "Random"
