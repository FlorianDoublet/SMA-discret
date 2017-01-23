from model.core.agent import Agent


class Defender(Agent):

    def __init__(self, color, x, y, environnement, is_trace, lifetime):
        super().__init__(color, x, y, environnement, is_trace)
        self.age = 0
        self.lifetime = lifetime

    def decide(self):
        self.age += 1

        if self.age >= self.lifetime:
            self.die()

    def print_cvs_change(self, cause):
        pass