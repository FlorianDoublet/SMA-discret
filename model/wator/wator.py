#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from itertools import product
from model.core.core import Core
from model.wator.Fish import Fish
from model.wator.Shark import Shark


class Wator(Core):

    def __init__(self):
        super().__init__()

    def init_agents(self):

        nb_fish = self.prop.nb_fish()
        nb_shark = self.prop.nb_shark()
        fish_breed_time = self.prop.breed_time_fish()
        shark_breed_time = self.prop.breed_time_shark()
        shark_starve_time = self.prop.starve_time_shark()

        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in product(range(max(self.w, self.h)), repeat=2)]

        index = 0
        if self.h > self.w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(self.w, self.h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = random.sample(every_possible_tuple_position, nb_fish+nb_shark)

        fish_positions = positions[nb_shark:]
        shark_positions = positions[:nb_shark]

        self.agent_list = []
        self.agent_list = [Fish(fish_breed_time, "green", p[1], p[0], self.environnement) for p in fish_positions]
        self.agent_list += [Shark(shark_breed_time,shark_starve_time, "pink", p[1], p[0], self.environnement) for p in shark_positions]

    def print_tick(self):
        print("Tick;" + str(self.tick))