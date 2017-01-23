from model.core.core import Core
from itertools import product
import random
from model.pacman.agents.defender import Defender
from model.pacman.agents.hunter import Hunter
from model.pacman.agents.wall import Wall
from model.pacman.cell import Cell
from model.pacman.agents.winner import Winner
from model.pacman.agents.avatar import Avatar
from model.pacman.pacman_env import PacmanEnv

import random

class Pacman(Core):

    def __init__(self):
        super().__init__()
        self.next_defender = 20
        #self.environnement = PacmanEnv(self.w, self.h, self)

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
        agent_pos = self.get_available_position()

        self.agent_list.append(Avatar("yellow", agent_pos[0], agent_pos[1],self.environnement, self.is_trace))

    def init_walls(self, type="random"):
        if type == "random":
            n_walls = 100
            agent_pos = random.sample(self.every_possible_tuple_position, n_walls)

            for pos in agent_pos:
                wall = Wall("brown", pos[0], pos[1], self.environnement)
                self.agent_list.append(wall)

        elif type == "labyrinth":
            self.generate_maze()

    def create_winner(self):
        agent_pos = self.get_available_position()

        winner = Winner("white", agent_pos[0], agent_pos[1], self.environnement, self.is_trace)
        self.environnement.set_agent(winner)
        self.agent_list.append(winner)

    def create_new_defender(self):
        agent_pos = self.get_available_position()

        defender = Defender("green", agent_pos[0], agent_pos[1], self.environnement, self.is_trace, 300)
        self.environnement.set_agent(defender)
        self.agent_list.append(defender)
        self.next_defender = 300

    def get_available_position(self):
        agent_pos = random.sample(self.every_possible_tuple_position, 1)
        agent_pos = agent_pos[0]
        position = self.environnement.get_grille()[agent_pos[1]][agent_pos[0]]

        while position is not None:
            agent_pos = random.sample(self.every_possible_tuple_position, 1)
            agent_pos = agent_pos[0]
            position = self.environnement.get_grille()[agent_pos[1]][agent_pos[0]]

        return agent_pos

    def generate_maze(self):
        self.maze = [[0 for x in range(self.w)] for y in range(self.h)]
        self.dx = [0, 1, 0, -1]
        self.dy = [-1, 0, 1, 0]  # directions to move in the maze
        self.gen_maze(0, 0)

        x = 0
        for i in self.maze:
            y=0
            for j in i:
                if j == 1:
                    wall = Wall("brown", x, y, self.environnement)
                    self.agent_list.append(wall)
                y += 1
            x += 1

    def gen_maze(self, cx, cy):
        self.maze[cy][cx] = 1
        while True:
            nlst = []
            for i in range(4):
                nx = cx + self.dx[i];
                ny = cy + self.dy[i]
                if nx >= 0 and nx < self.w and ny >= 0 and ny < self.h:
                    if self.maze[ny][nx] == 0:
                        ctr = 0
                        for j in range(4):
                            ex = nx + self.dx[j];
                            ey = ny + self.dy[j]
                            if ex >= 0 and ex < self.w and ey >= 0 and ey < self.h:
                                if self.maze[ey][ex] == 1: ctr += 1
                        if ctr == 1: nlst.append(i)
            if len(nlst) > 0:
                ir = nlst[random.randint(0, len(nlst) - 1)]
                cx += self.dx[ir];
                cy += self.dy[ir]
                self.gen_maze(cx, cy)
            else:
                break