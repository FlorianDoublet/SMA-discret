from graphics import *
from observerPattern.observer import Observer


class Vue(Observer):
    def __init__(self, w, h):
        self.window = GraphWin('TP1', w, h)

        self.window.setBackground("darkblue")

    def update(self, *args, **kwargs):
        agents = args[0]

        for agent in agents:
            pt = Point(agent.x, agent.y)
            pt.setFill("white")
            pt.draw(self.window)

    def end_draw(self):
        self.window.getMouse()
        self.window.close()
