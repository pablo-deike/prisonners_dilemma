from strategies.no_memory_strategy import NoMemoryStrategy

import random


class RandomStrategy(NoMemoryStrategy):

    def play(self) -> bool:
        return random.uniform(0, 1) <= 0.5

    def __str__(self) -> str:
        super().__str__()
        return "Random"
