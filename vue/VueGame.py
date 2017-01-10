from observerPattern.observer import Observer
import pygame
from pygame.locals import *

class VueGame(Observer):


    def __init__(self, w, h, box_size):
        self.w = w
        self.h = h
        self.box_size = box_size

        self.key_to_function = {
            pygame.K_LEFT: (lambda x: x.scroll(dx=1)),
            pygame.K_RIGHT: (lambda x: x.scroll(dx=-1)),
            pygame.K_DOWN: (lambda x: x.scroll(dy=-1)),
            pygame.K_UP: (lambda x: x.scroll(dy=1)),
            pygame.K_EQUALS: (lambda x: x.zoom(2)),
            pygame.K_MINUS: (lambda x: x.zoom(0.5)),
            pygame.K_r: (lambda x: x.reset())}

        self.clock = pygame.time.Clock()
        pygame.init()
        self.window = pygame.display.set_mode(((w*box_size), (h*box_size)))
        self.universe_screen = UniverseScreen((w*box_size), (h*box_size))
        self.window.set_alpha(None) #Speeding up by removing the alpha channel

    def draw_grid(self):
        h = self.h * self.box_size
        w = self.w * self.box_size

        offset_x = int(self.universe_screen.mx + (self.universe_screen.dx) * self.universe_screen.magnification)
        offset_y = int(self.universe_screen.my + (self.universe_screen.dy) * self.universe_screen.magnification)

        box_size = int(self.box_size * self.universe_screen.magnification)

        if self.box_size > 1:
            for i in range(0, h-offset_y, box_size):
                pygame.draw.line(self.window, Color('black'), (offset_x, i+offset_y), (w+offset_x, i+offset_y))

            for j in range(0, w-offset_x, box_size):
                pygame.draw.line(self.window, Color('black'), (j+offset_x, offset_y), (j+offset_x, h+offset_y))

    def update(self, *args, **kwargs):
        #self.clock.tick(60)  # 60 frame per second

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_to_function:
                    self.key_to_function[event.key](self.universe_screen)
                elif event.key == pygame.K_SPACE:
                    paused = (True, False)[paused]

        environnement = args[0]
        agents = environnement.SMA.agent_list

        self.window.fill(Color('darkblue'))
        self.draw_grid()

        for agent in agents:
            ax=agent.x*self.box_size+int(self.box_size/2)
            ay=agent.y*self.box_size+int(self.box_size/2)
            asize = int(self.box_size/2)

            x = int(self.universe_screen.mx + (self.universe_screen.dx + ax) * self.universe_screen.magnification)
            y = int(self.universe_screen.my + (self.universe_screen.dy + ay) * self.universe_screen.magnification)
            size = int(asize * self.universe_screen.magnification)

            pygame.draw.circle(self.window,
                               Color(agent.color),
                               (x,y),
                               size)

        pygame.display.flip()


class UniverseScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        (self.dx, self.dy) = (0, 0)
        (self.mx, self.my) = (0, 0)
        self.magnification = 1.0

    def scroll(self, dx=0, dy=0):
        self.dx += dx * self.width / (self.magnification * 10)
        self.dy += dy * self.height / (self.magnification * 10)

    def zoom(self, zoom):
        self.magnification *= zoom
        self.mx = (1 - self.magnification) * self.width / 2
        self.my = (1 - self.magnification) * self.height / 2

    def reset(self):
        (self.dx, self.dy) = (0, 0)
        (self.mx, self.my) = (0, 0)
        self.magnification = 1.0