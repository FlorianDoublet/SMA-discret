
from graphics import *

class Vue:

    def __init__(self, ):
        self.window = GraphWin('TP1', 500, 500)
        self.window.setCoords(0.0, 0.0, 10.0, 10.0)
        self.window.setBackground("black")

        self.window.getMouse()
        self.window.close()

Vue()