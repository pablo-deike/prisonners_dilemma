from strategies.strategy import Strategy


class TitForTatStrategy(Strategy):

    def play(self, last_plays: list) -> bool:
        if last_plays[-1] is True:
            return True
        return False

    def __str__(self):
        super().__str__()
        return "Tit for tat"
