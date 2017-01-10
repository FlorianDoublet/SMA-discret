from tkinter import *
from observerPattern.observer import Observer
from utils.PropertiesReader import PropertiesReader

class Vue(Observer):
    def __init__(self):
        self.prop = PropertiesReader.prop
        self.w, self.h = self.prop.grid_size()
        self.box_size = self.prop.box_size()
        self.tick = 0
        self.refresh = self.prop.refresh()
        self.fen = Tk()
        fen_w, fen_h = self.prop.canvas_size()
        # taille en pixel pour la fenetre
        self.fen.geometry(str(fen_w) + 'x' + str(fen_h))

        self.canvas = Canvas(self.fen, bg=self.prop.canvas_background_color(), height=self.h*self.box_size, width=self.w*self.box_size)
        self.canvas.pack()
        self.repaint()

    def draw_grid(self):
        if not self.prop.print_grid():
            return
        grid_color = self.prop.grid_color()
        if self.box_size > 1:
            for i in range(0, self.h * self.box_size, self.box_size):
                self.canvas.create_line(0, i, self.w*self.box_size, i, fill=grid_color)

            for j in range(0, self.w * self.box_size, self.box_size):
                self.canvas.create_line(j, 0, j, self.h*self.box_size, fill=grid_color)

    def update(self, *args, **kwargs):
        env = args[0]
        self.canvas.delete("all")
        self.draw_grid()
        agents = env.SMA.agent_list

        for agent in agents:
            id = self.canvas.create_oval(0, 0, self.box_size, self.box_size, fill=agent.color, outline='black')
            self.canvas.move(id, agent.x*self.box_size, agent.y*self.box_size)

        if (self.tick % self.refresh) == 0:
            self.repaint()
        self.tick += 1

    def repaint(self):
        self.fen.update_idletasks()
        self.fen.update()

    def end_draw(self):
        pass
