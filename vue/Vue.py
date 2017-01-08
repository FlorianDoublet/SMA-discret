from graphics import *
from model.Agent import *
from model.Environnement import *
from observerPattern.observer import Observer


class Vue(Observer):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.window = GraphWin('TP1', self.w, self.h)
        self.cell_color = "darkblue"
        self.window.setBackground(self.cell_color)

    def update(self, *args, **kwargs):
        environnement = args[0]
        agents = environnement.SMA.agent_list

        for agent in agents:
            pt = Point(agent.x, agent.y)
            pt.setFill(agent.color)
            pt.draw(self.window)
        self.window.delete("all")

    def end_draw(self):
        self.window.getMouse()
        self.window.close()
