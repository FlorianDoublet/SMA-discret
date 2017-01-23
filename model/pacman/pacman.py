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
        self.next_defender = 20
        self.environnement = PacmanEnv(self.w, self.h, self)


    def init_agents(self):
        # Generer toutes les permutations possibles
        self.every_possible_tuple_position = [i for i in product(range(max(self.w, self.h)), repeat=2)]

        index = 0
        if self.h > self.w:
            index = 1

        self.every_possible_tuple_position = [i for i in self.every_possible_tuple_position if i[index] < min(self.w, self.h)]

        # Recuperer x valeurs de toutes les permutations possible sans doublons

        self.agent_list = []
        self.init_walls()
        self.init_avatar()

    def print_tick(self):
        pass

    def run(self):
        super().run()
        self.next_defender -= 1
        if self.next_defender <= 0:
            self.create_new_defender()

    def init_avatar(self):
        agent_pos = random.sample(self.every_possible_tuple_position, 1)
        agent_pos = agent_pos[0]
        position = self.environnement.get_grille()[agent_pos[1]][agent_pos[0]]

        while position is not None:
            agent_pos = random.sample(self.every_possible_tuple_position, 1)
            agent_pos = agent_pos[0]
            position = self.environnement.get_grille()[agent_pos[1]][agent_pos[0]]

        self.agent_list.append(Avatar("yellow", agent_pos[0], agent_pos[1],self.environnement, self.is_trace))

    def init_walls(self, type="random"):
        if type == "random":
            n_walls = 100
            agent_pos = random.sample(self.every_possible_tuple_position, n_walls)

            for pos in agent_pos:
                wall = Wall("brown", pos[0], pos[1], self.environnement)
                self.agent_list.append(wall)


        elif type == "labyrinth":
            pass


    def create_new_defender(self):
        agent_pos = random.sample(self.every_possible_tuple_position, 1)
        agent_pos = agent_pos[0]
        position = self.environnement.get_grille()[agent_pos[1]][agent_pos[0]]

        while position is not None :
            agent_pos = random.sample(self.every_possible_tuple_position, 1)
            agent_pos = agent_pos[0]
            position = self.environnement.get_grille()[agent_pos[1]][agent_pos[0]]

        defender = Defender("green", agent_pos[0], agent_pos[1], self.environnement, self.is_trace, 100)
        self.environnement.set_agent(defender)
        self.agent_list.append(defender)
        self.next_defender = 100







