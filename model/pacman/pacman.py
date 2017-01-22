from model.core.core import Core
from itertools import product
from model.pacman.agents.defender import Defender
from model.pacman.agents.hunter import Hunter
from model.pacman.agents.wall import Wall
from model.pacman.agents.winner import Winner
from model.pacman.agents.avatar import Avatar

import random

class Pacman(Core):

    def __init__(self):
        super().__init__()
        self.next_defender = 20


    def init_agents(self):
        # Generer toutes les permutations possibles
        self.every_possible_tuple_position = [i for i in product(range(max(self.w, self.h)), repeat=2)]

        index = 0
        if self.h > self.w:
            index = 1

        self.every_possible_tuple_position = [i for i in self.every_possible_tuple_position if i[index] < min(self.w, self.h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = random.sample(self.every_possible_tuple_position, 1)

        self.agent_list = []
        agent_pos = positions[0]
        self.agent_list.append(Avatar("yellow", agent_pos[0], agent_pos[1],self.environnement, self.is_trace))

    def print_tick(self):
        pass

    def run(self):
        super().run()
        self.next_defender -= 1
        if self.next_defender <= 0:
            self.create_new_defender()

    def create_new_defender(self):
        agent_pos = random.sample(self.every_possible_tuple_position, 1)
        agent_pos = agent_pos[0]
        defender = Defender("green", agent_pos[0], agent_pos[1], self.environnement, self.is_trace, 500)
        self.environnement.set_agent(defender)
        self.agent_list.append(defender)
        self.next_defender = 500







