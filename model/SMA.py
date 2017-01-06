from random import sample
from itertools import product
from model.Agent import Agent
from observerPattern.observable import Observable


class SMA(Observable):
    def __init__(self, w, h, number):
        super().__init__()

        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in product(range(max(w, h)), repeat=2)]
        for p in every_possible_tuple_position:
            print(p)

        index = 0
        if h > w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(w, h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = sample(every_possible_tuple_position, number)

        # On cree les agents
        self.agent_list = [Agent("color", p[0], p[1]) for p in positions]

    def run(self):
        pass