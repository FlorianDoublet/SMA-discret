
class Environnement:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grille2d = [[None for x in range(self.w)] for y in range(self.h)]


