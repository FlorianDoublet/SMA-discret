from observerPattern.observer import Observer
import pygame
from pygame.locals import *

#sudo apt-get install python-pygame

class VueGame(Observer):
    def __init__(self, w, h, box_size):
        self.w = w
        self.h = h
        self.box_size = box_size

        pygame.init()
        self.window = pygame.display.set_mode((w*box_size, h*box_size), RESIZABLE)

    def draw_grid(self):
        '''if self.box_size > 1:
            for i in range(0, self.w * self.box_size, self.box_size):
                self.canvas.create_line(0, i, self.h*self.box_size, i, fill='black')

            for j in range(0, self.h * self.box_size, self.box_size):
                self.canvas.create_line(j, 0, j, self.h*self.box_size, fill='black')'''
        pass

    def update(self, *args, **kwargs):
        environnement = args[0]
        self.window.delete("all")
        self.draw_grid()
        agents = environnement.SMA.agent_list

        for agent in agents:
            id = pygame.draw.circle(self.window, agent.color, (agent.x*self.box_size, agent.y*self.box_size), self.box_size, 0)

            #(0, 0, self.box_size, self.box_size, fill=agent.color, outline='black')
            #self.canvas.move(id, agent.x*self.box_size, agent.y*self.box_size)