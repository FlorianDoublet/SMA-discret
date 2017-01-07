from random import randrange


class Agent:

    _directions = ["up", "down", "right", "left", "up-right", "up-left", "down-right", "down-left"]

    def __init__(self, color, x, y, environnement):
        self.color = color
        self.x = x
        self.y = y
        self.environnement = environnement
        # un agent s'ajoute lui meme dans l'environnement dans l'initialisation
        self.environnement.grille2d[y][x] = self
        self.default_direction = self.random_direction()

    def decide(self):
        pass

    def random_direction(self):
        direction_size = len(self._directions)
        return self._directions[randrange(direction_size)]
