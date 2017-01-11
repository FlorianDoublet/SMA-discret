from tkinter import *
from observerPattern.observer import Observer
from utils.PropertiesReader import PropertiesReader

import platform


class Vue(Observer):
    OS = platform.system()

    def __init__(self):
        self.prop = PropertiesReader.prop
        self.w, self.h = self.prop.grid_size()
        self.box_size = self.prop.box_size()
        self.tick = 0
        self.refresh = self.prop.refresh()
        self.fen = Tk()
        max_height_size = self.h*self.box_size
        max_width_size = self.w*self.box_size
        self.fen.maxsize(width=max_width_size+22, height=max_height_size+22)
        fen_w, fen_h = self.prop.canvas_size()
        frame = Frame(self.fen, width=fen_w, height=fen_h)
        frame.grid(row=0, column=0)
        frame.pack(fill=BOTH, expand=YES)
        self.canvas = Canvas(frame, bg=self.prop.canvas_background_color(), height=max_height_size, width=max_width_size, scrollregion=(0,0,max_width_size,max_height_size))

        # with Windows OS
        """self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        # with Linux OS
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)"""

        if self.OS == "Linux":
            self.canvas.bind_all('<4>', self.onMouseWheel, add='+')
            self.canvas.bind_all('<5>', self.onMouseWheel, add='+')
        else:
            # Windows and MacOS
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel, add='+')

        hbar = Scrollbar(frame, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(frame, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(width=fen_w, height=fen_h)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
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
            id = self.canvas.create_oval(1, 1, self.box_size-1, self.box_size-1, fill=agent.color, outline=agent.color)
            self.canvas.move(id, agent.x*self.box_size, agent.y*self.box_size)

        if (self.tick % self.refresh) == 0:
            self.repaint()
        self.tick += 1

    def repaint(self):
        self.fen.update_idletasks()
        self.fen.update()

    def end_draw(self):
        pass

    def _on_mousewheel(self, event):
        print(event.delta)
        self.canvas.yview_scroll(-1 * (event.delta / 120), "units")

    def onMouseWheel(self, event):
        factor=1

        if self.OS == 'Linux':
            if event.num == 4:
                self.canvas.yview_scroll((-1) * factor, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(factor, "units")

        elif self.OS == 'Windows':
            self.canvas.yview_scroll((-1) * int((event.delta / 120) * factor), "units")


