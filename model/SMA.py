#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from itertools import product
from model.Agent import Agent
from model.Environnement import Environnement
from observerPattern.observable import Observable
from utils.PropertiesReader import PropertiesReader
import tkinter

class SMA(Observable):

    def __init__(self):
        super().__init__()
        self.prop = PropertiesReader.prop
        self.tick = 1
        w, h = self.prop.grid_size()
        number = self.prop.nb_particles()
        self.sheduling = self.prop.sheduling()
        seed = self.prop.random_seed()
        if seed != 0:
            random.seed(seed)

        # On cree l'environnement
        self.environnement = Environnement(w, h, self)

        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in product(range(max(w, h)), repeat=2)]

        index = 0
        if h > w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(w, h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = random.sample(every_possible_tuple_position, number)

        # On cree les agents
        self.agent_list = [Agent(self.random_color(), p[1], p[0], self.environnement) for p in positions]

    def run(self):
        """
        effectue le tour de parole
        :return:
        """
        list_after_schedule = self.apply_sheduling()

        # on lance donc en fonction  de l'ordre random la methode .decide sur l'agent qu'on pioche dans la liste des agents
        for agent in list_after_schedule:
            agent.decide()

        # on notifie les observers que l'environnement a change
        self.set_changed()
        self.notify_observers(self.environnement)
        if self.prop.trace():
            self.print_tick()
        self.tick += 1

    def random_color(self):
        d = random.randint(0, 255)
        r = random.randint(0, 255)
        w = random.randint(0, 255)
        mix = self.prop.random_mix_color()
        if mix :
            d = int((d + mix[0]) / 2)
            r = int((r + mix[0]) / 2)
            w = int((w + mix[0]) / 2)

        de = ("%02x" % d)
        re = ("%02x" % r)
        we = ("%02x" % w)
        ge = "#"
        color = ge + de + re + we
        return color

    def print_tick(self):
        print("Tick;"+str(self.tick))


    def apply_sheduling(self):
        if self.sheduling == "equitable":
            random.shuffle(self.agent_list)
            return self.agent_list
        elif self.sheduling == "sequential":
            return self.agent_list
        elif self.sheduling == "random":
            size = len(self.agent_list)
            random_order = []
            for i in range(size):
                random_order.append(self.agent_list[random.randrange(size)])
            return random_order
