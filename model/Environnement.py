
class Environnement:

    def __init__(self, w, h, SMA, is_torrique):
        self.w = w
        self.h = h
        self.grille2d = [[None for x in range(self.w)] for y in range(self.h)]
        self.SMA = SMA
        self.is_torrique = is_torrique






