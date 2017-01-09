from tkinter import *
from observerPattern.observer import Observer


class Vue(Observer):
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.fen = Tk()
        self.canvas = Canvas(self.fen, bg="darkblue", height=h, width=w)
        self.canvas.pack()
        self.fen.update_idletasks()
        self.fen.update()

    def update(self, *args, **kwargs):
        environnement = args[0]
        self.canvas.delete("all")
        agents = environnement.SMA.agent_list

        for agent in agents:
            id = self.canvas.create_oval(-5, -5, 5, 5, fill=agent.color, outline='black')
            id2 = self.canvas.create_oval(0, 0, 0, 0, fill='white', outline='')
            self.canvas.move(id, agent.x, agent.y)
            self.canvas.move(id2, agent.x, agent.y)

        self.fen.update_idletasks()
        self.fen.update()

    def end_draw(self):
        self.window.getMouse()
        self.window.close()
