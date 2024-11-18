from include.player import Player
from include.points_decider import points_decider
from strategies.defector_strategy import DefectorStrategy
from strategies.random_strategy import RandomStrategy
from strategies.strategy import Strategy
from strategies.tit_for_tat_strategy import TitForTatStrategy
from get_all_strategies import get_all_strategies


def play() -> None:
    player_1 = Player()
    player_2 = Player()
    strategies = get_all_strategies()
    for i in range(len(strategies) - 1):
        strategy_1 = strategies[i](player_1)
        for j in range(i + 1, len(strategies)):
            strategy_2 = strategies[j](player_2)
            simulate(strategy_1, strategy_2, 100)

    print(
        f"Player 1 with strategy {strategy_1} has {player_1.points} points and Player 2 with strategy {strategy_2} has {player_2.points} points"
    )


def simulate(strategy_1: Strategy, strategy_2: Strategy, rounds: int) -> None:
    for i in range(rounds):
        strategy_1.play()
        strategy_2.play()
        points_decider(strategy_1.player, strategy_2.player)


play()
