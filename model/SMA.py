from random import sample
from itertools import combinations_with_replacement
from model.Agent import Agent


class SMA:

    def __init__(self, w, h):

        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in combinations_with_replacement(range(max(w, h)), 2)]

        index = 0
        if h > w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(w, h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = sample(every_possible_tuple_position, 10)

        # On cree les agents
        self.agent_list = [Agent("color", p[0], p[1]) for p in positions]

    def run(self):
        pass