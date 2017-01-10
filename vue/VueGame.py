from observerPattern.observer import Observer
import pygame
from pygame.locals import *

class VueGame(Observer):
    def __init__(self, w, h, box_size):
        self.w = w
        self.h = h
        self.box_size = box_size

        self.clock = pygame.time.Clock()
        pygame.init()
        self.window = pygame.display.set_mode((w*box_size, h*box_size))
        self.window.set_alpha(None) #Speeding up by removing the alpha channel

    def draw_grid(self):
        if self.box_size > 1:
            for i in range(0, self.h * self.box_size, self.box_size):
                pygame.draw.line(self.window, Color('black'), (0, i), (self.w*self.box_size, i))

            for j in range(0, self.w * self.box_size, self.box_size):
                pygame.draw.line(self.window, Color('black'), (j, 0), (j, self.h*self.box_size))

    def update(self, *args, **kwargs):
        #self.clock.tick(60)  # 60 frame per second

        environnement = args[0]
        agents = environnement.SMA.agent_list

        self.window.fill(Color('darkblue'))
        self.draw_grid()

        for agent in agents:
            pygame.draw.circle(self.window,
                               Color(agent.color),
                               (agent.x*self.box_size+int(self.box_size/2),
                                agent.y*self.box_size+int(self.box_size/2)),
                               int(self.box_size/2))

        pygame.display.flip()
