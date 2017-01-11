#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc
import random

from model.core.Environnement import Environnement
from observerPattern.observable import Observable
from utils.PropertiesReader import PropertiesReader


class Core(Observable):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        super().__init__()
        self.prop = PropertiesReader.prop
        self.tick = 1
        self.w, self.h = self.prop.grid_size()
        self.sheduling = self.prop.sheduling()
        seed = self.prop.random_seed()
        if seed != 0:
            random.seed(seed)

        # On cree l'environnement
        self.environnement = Environnement(self.w, self.h, self)
        self.init_agents()


    @abc.abstractmethod
    def init_agents(self):
        pass



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
            r = int((r + mix[1]) / 2)
            w = int((w + mix[2]) / 2)

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
