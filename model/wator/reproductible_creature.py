import abc
from model.core.agent import Agent


class ReproductibleCreature(Agent):
    __metaclass__ = abc.ABCMeta
    """
    class for all the reproductible creature agent
    """

    def __init__(self, breed_time, color, x, y, env):
        super().__init__(color, x, y, env)
        self.breed_time = breed_time
        self.age = 0
        self.maturity = 0

    def die(self):
        self.environnement.get_grille()[self.y][self.x] = None
        self.environnement.SMA.agent_list.remove(self)

    @abc.abstractmethod
    def reproduce(self, x, y):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def decide(self):
        pass

    @abc.abstractmethod
    def print_direct_change(self, cause):
        pass
