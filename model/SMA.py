from random import sample
from itertools import product
from model.Agent import Agent
from model.Environnement import Environnement
from observerPattern.observable import Observable


class SMA(Observable):

    def __init__(self, w, h, number):
        super().__init__()

        # On cree l'environnement
        self.environnement = Environnement(w, h, self, False)

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
        self.agent_list = [Agent("color", p[0], p[1], self.environnement) for p in positions]


    def run(self):
        agents_size = len(self.agent_list)
        # cree un random de la taille de la liste d'agent, avec aucun doublon, donc de 0 à taille de la liste
        random_order = sample(range(0, agents_size), agents_size)
        # on lance donc en fonction de l'ordre random la methode .decide sur l'agent qu'on pioche dans la liste des agents
        map(lambda x: self.agent_list[x].decide(), random_order)
