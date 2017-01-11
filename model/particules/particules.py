#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from itertools import product
from model.particules.particule import Particle
from model.core.core import Core


class Particles(Core):

    def __init__(self):
        super().__init__()

    def init_agents(self):
        number = self.prop.nb_particles()

        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in product(range(max(self.w, self.h)), repeat=2)]

        index = 0
        if self.h > self.w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(self.w, self.h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = random.sample(every_possible_tuple_position, number)

        # On cree les agents
        self.agent_list = [Particle(self.random_color(), p[1], p[0], self.environnement) for p in positions]

