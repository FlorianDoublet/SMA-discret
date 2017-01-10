from tkinter import *
from observerPattern.observer import Observer


class Vue(Observer):
    def __init__(self, w, h, box_size):
        self.w = w
        self.h = h
        self.box_size = box_size
        self.fen = Tk()
        self.canvas = Canvas(self.fen, bg="darkblue", height=h*self.box_size, width=w*self.box_size)
        self.canvas.pack()
        self.fen.update_idletasks()
        self.fen.update()

    def draw_grid(self):
        if self.box_size > 1:
            for i in range(0, self.h * self.box_size, self.box_size):
                self.canvas.create_line(0, i, self.w*self.box_size, i, fill='black')

            for j in range(0, self.w * self.box_size, self.box_size):
                self.canvas.create_line(j, 0, j, self.h*self.box_size, fill='black')

    def update(self, *args, **kwargs):
        environnement = args[0]
        self.canvas.delete("all")
        self.draw_grid()
        agents = environnement.SMA.agent_list

        for agent in agents:
            id = self.canvas.create_oval(0, 0, self.box_size, self.box_size, fill=agent.color, outline='black')
            self.canvas.move(id, agent.x*self.box_size, agent.y*self.box_size)

        self.fen.update_idletasks()
        self.fen.update()

    def end_draw(self):
        pass
