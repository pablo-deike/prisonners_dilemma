from strategies.no_memory_strategy import NoMemoryStrategy

import random


class RandomStrategy(NoMemoryStrategy):

    def play(self, last_plays: list) -> bool:
        return random.uniform(0, 1) <= 0.5

    def __str__(self):
        super().__str__()
        return "Random"
