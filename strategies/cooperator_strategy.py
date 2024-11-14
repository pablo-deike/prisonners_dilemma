from strategies.no_memory_strategy import NoMemoryStrategy


class CooperatorStrategy(NoMemoryStrategy):

    def play(self, last_plays) -> bool:
        return False

    def __str__(self) -> str:
        return "Unconditional cooperator"
