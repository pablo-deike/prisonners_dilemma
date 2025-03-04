from typing import Optional
from player.player import Player

import random

from strategies.strategy import Strategy


class RandomPStrategy(Strategy):

    def __init__(self, player: Player, probability: Optional[float] = None):
        self.player = player
        self.probability = probability or random.uniform(0, 1)
        self.scores = []

    def play(self) -> bool:
        return self.player.play(random.uniform(0, 1) <= self.probability)

    def get_final_score(self, points: int) -> None:
        self.scores.append(points)

    def get_average_scores(self) -> None:
        self.avg_score = sum(self.scores) / len(self.scores)

    def __str__(self) -> str:
        super().__str__()
        return f"Random with probability p={self.probability}"
