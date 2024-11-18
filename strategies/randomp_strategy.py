from typing import Optional
from include.player import Player

import random

from strategies.strategy import Strategy


class RandomPStrategy(Strategy):

    def __init__(self, player: Player, probability: Optional[float] = None):
        self.player = player
        self.probability = probability or random.uniform(0, 1)

    def play(self) -> bool:
        return self.player.play(random.uniform(0, 1) <= self.probability)

    def __str__(self) -> str:
        super().__str__()
        return f"Random with probability p={self.probability}"
