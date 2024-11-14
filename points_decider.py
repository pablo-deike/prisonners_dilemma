from player import Player


def points_decider(player_1: Player, player_2: Player) -> None:
    if player_1.conflict is True and player_2.conflict is True:
        player_1.change_points(1)
        player_2.change_points(1)
    if player_1.conflict is True and player_2.conflict is False:
        player_1.change_points(5)
        player_2.change_points(0)
    if player_1.conflict is False and player_2.conflict is True:
        player_1.change_points(0)
        player_2.change_points(5)
    if player_1.conflict is False and player_2.conflict is False:
        player_1.change_points(3)
        player_2.change_points(3)
