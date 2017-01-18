from model.core.agent import Agent


class Hunter(Agent):

    def __init__(self, color, x, y, environnement, is_trace):
        super().__init__(color, x, y, environnement, is_trace)