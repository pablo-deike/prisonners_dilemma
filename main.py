from include.player import Player
from include.points_decider import points_decider
from strategies.defector_strategy import DefectorStrategy
from strategies.random_strategy import RandomStrategy
from strategies.tit_for_tat_strategy import TitForTatStrategy


def play() -> None:
    player_1 = Player()
    player_2 = Player()
    strategy_1 = DefectorStrategy(player_1)
    strategy_2 = RandomStrategy(player_2)
    for i in range(10):
        strategy_1.play()
        strategy_2.play()
        points_decider(player_1, player_2)

    print(
        f"Player 1 with strategy {strategy_1} has {player_1.points} points and Player 2 with strategy {strategy_2} has {player_2.points} points"
    )


play()
