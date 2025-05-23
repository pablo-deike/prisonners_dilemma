from player.player import Player


def points_decider(player_1: Player, player_2: Player) -> None:
    if player_1.defects is True and player_2.defects is True:
        player_1.add_points(1)
        player_2.add_points(1)
        player_1.add_opposing_plays(player_2.defects)
        player_2.add_opposing_plays(player_1.defects)
    if player_1.defects is True and player_2.defects is False:
        player_1.add_points(5)
        player_2.add_points(0)
        player_1.add_opposing_plays(player_2.defects)
        player_2.add_opposing_plays(player_1.defects)
    if player_1.defects is False and player_2.defects is True:
        player_1.add_points(0)
        player_2.add_points(5)
        player_1.add_opposing_plays(player_2.defects)
        player_2.add_opposing_plays(player_1.defects)
    if player_1.defects is False and player_2.defects is False:
        player_1.add_points(3)
        player_2.add_points(3)
        player_1.add_opposing_plays(player_2.defects)
        player_2.add_opposing_plays(player_1.defects)
