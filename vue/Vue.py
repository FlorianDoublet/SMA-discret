from graphics import *
from model.Agent import *
from model.Environnement import *
from observerPattern.observer import Observer


class Vue(Observer):
    def __init__(self, w, h):
        self.window = GraphWin('TP1', w, h)
        self.cell_color = "darkblue"

        self.window.setBackground(self.cell_color)

    def update(self, *args, **kwargs):
        environnement = args[0]
        grille = environnement.get_grille()

        for y in range(len(grille)):
            for x in range(len(grille[y])):
                cell = grille[y][x]
                pt = Point(x, y)
                pt.draw(self.window)
                if not cell:
                    # si c'est None, et donc une case vide
                    pt.setFill(self.cell_color)
                elif type(cell) is Agent:
                    agent = cell
                    pt.setFill(agent.color)

                pt.draw(self.window)

    def end_draw(self):
        self.window.getMouse()
        self.window.close()
