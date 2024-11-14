from include.player import Player
from include.points_decider import points_decider
from strategies.random_strategy import RandomStrategy
from strategies.tit_for_tat_strategy import TitForTatStrategy


def play() -> None:
    player_1 = Player(TitForTatStrategy())
    player_2 = Player(RandomStrategy())
    for i in range(10):
        player_1.play(player_2.plays[0:i])
        player_2.play(player_1.plays[0:i])
        points_decider(player_1, player_2)

    print(
        f"Player 1 with strategy {player_1.strategy} has {player_1.points} points and Player 2 with strategy {player_2.strategy} has {player_2.points} points"
    )


play()
