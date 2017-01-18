from model.core.agent import Agent


class Wall(Agent):

    def __init__(self, color, x, y, environnement):
        super().__init__(color, x, y, environnement, False)

