from tkinter import *
from model.Agent import *
from model.Environnement import *
from observerPattern.observer import Observer


class Vue(Observer):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.fen = Tk()
        self.canvas = Canvas(self.fen, bg="blue", height=h, width=w)
        self.canvas.pack()
        self.fen.update_idletasks()
        self.fen.update()


    def update(self, *args, **kwargs):
        environnement = args[0]
        self.canvas.delete("all")
        agents = environnement.SMA.agent_list
        for agent in agents:
            id = self.canvas.create_oval(10, 10, 25, 25, fill=agent.color)
            self.canvas.move(id, agent.x, agent.y)

        self.fen.update_idletasks()
        self.fen.update()





    def end_draw(self):
        self.window.getMouse()
        self.window.close()
