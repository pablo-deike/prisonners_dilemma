class Player:

    def __init__(self):
        self.points = 0
        self.conflict = False

    def change_points(self, points: int) -> None:
        self.points += points

    def play_conflict(self) -> None:
        self.conflict = True

    def play_cooperation(self) -> None:
        self.conflict = False
