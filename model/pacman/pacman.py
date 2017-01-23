from model.core.core import Core
from itertools import product
from model.pacman.agents.defender import Defender
from model.pacman.agents.hunter import Hunter
from model.pacman.agents.wall import Wall
from model.pacman.agents.winner import Winner
from model.pacman.agents.avatar import Avatar
from model.pacman.pacman_env import PacmanEnv

import random

class Pacman(Core):

    def __init__(self):
        super().__init__()
        self.environnement = PacmanEnv(self.w, self.h, self)


    def init_agents(self):
        # Generer toutes les permutations possibles
        every_possible_tuple_position = [i for i in product(range(max(self.w, self.h)), repeat=2)]

        index = 0
        if self.h > self.w:
            index = 1

        every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(self.w, self.h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons
        positions = random.sample(every_possible_tuple_position, 1)

        self.agent_list = []
        agent_pos = positions[0]
        self.agent_list.append(Avatar("yellow", agent_pos[0], agent_pos[1],self.environnement, self.is_trace))


    def print_tick(self):
        pass
