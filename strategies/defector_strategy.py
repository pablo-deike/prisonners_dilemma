from strategies.no_memory_strategy import NoMemoryStrategy


class DefectorStrategy(NoMemoryStrategy):

    def play(self) -> bool:
        return True

    def __str__(self) -> str:
        return "Unconditional cooperator"
