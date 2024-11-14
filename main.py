from player import Player
from points_decider import points_decider


def play() -> None:
    player_1 = Player()
    player_2 = Player()

    player_2.play_conflict()
    points_decider(player_1, player_2)

    print(f"Player 1 points:{player_1.points} and Player 2 points: {player_2.points}")


play()
