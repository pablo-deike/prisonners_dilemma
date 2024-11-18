from include.player import Player
from include.points_decider import points_decider
from strategies.strategy import Strategy
from get_all_strategies import get_all_strategies


def play() -> None:
    strategies_classes = get_all_strategies()
    strategies: list[Strategy] = []
    final_scores = {}
    for strategy_class in strategies_classes:
        strategies.append(strategy_class(Player()))
    for i in range(len(strategies_classes) - 1):
        for j in range(i + 1, len(strategies_classes)):
            simulate(strategy_1=strategies[i], strategy_2=strategies[j], rounds=100)
    for strategy in strategies:
        strategy.get_average_scores()
        final_scores[str(strategy)] = strategy.avg_score
        print(f"{strategy} final score: {strategy.scores}\n")
    print(final_scores)


def simulate(strategy_1: Strategy, strategy_2: Strategy, rounds: int) -> None:
    for _ in range(rounds):
        strategy_1.play()
        strategy_2.play()
        points_decider(strategy_1.player, strategy_2.player)
    strategy_1.get_final_score(strategy_1.player.points)
    strategy_2.get_final_score(strategy_2.player.points)
    strategy_1.player.reset_player()
    strategy_2.player.reset_player()


play()
