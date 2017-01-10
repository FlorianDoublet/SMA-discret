#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import sample, randrange, shuffle
from itertools import product
from model.Agent import Agent
from model.Environnement import Environnement
from observerPattern.observable import Observable


class SMA(Observable):

    _color_list = ["white", "red", "green", "yellow"]

    def __init__(self, w, h, number):
        super().__init__()

        # On cree l'environnement
        self.environnement = Environnement(w, h, self, True)

        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in product(range(max(w, h)), repeat=2)]

        index = 0
        if h > w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(w, h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = sample(every_possible_tuple_position, number)

        # On cree les agents
        self.agent_list = [Agent(self.random_color(), p[1], p[0], self.environnement) for p in positions]

    def run(self):
        """
        effectue le tour de parole
        :return:
        """
        agents_size = len(self.agent_list)
        # cree un random de la taille de la liste d'agent, avec aucun doublon, donc de 0 à taille de la liste
        #random_order = sample(range(0, agents_size), agents_size)
        shuffle(self.agent_list)

        # on lance donc en fonction  de l'ordre random la methode .decide sur l'agent qu'on pioche dans la liste des agents

        """for i in range(agents_size):
            self.agent_list[i].decide()"""
        for agent in self.agent_list:
            agent.decide()

        # on notifie les observers que l'environnement a change
        # et on leurs donne donc l'environnement
        # a note on ne notifie que lorsque tout a bouge
        self.set_changed()
        self.notify_observers(self.environnement)

    def random_color(self):
        color_list_size = len(self._color_list)
        return self._color_list[randrange(color_list_size)]
