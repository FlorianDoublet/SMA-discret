from graphics import *
from observerPattern.observer import Observer


class Vue(Observer):
    def test():
        win = GraphWin('Face', 200, 150)  # give title and dimensions

        head = Circle(Point(40, 100), 25)  # set center and radius
        head.setFill("yellow")
        head.draw(win)

        eye1 = Circle(Point(30, 105), 5)
        eye1.setFill('blue')
        eye1.draw(win)

        eye2 = Line(Point(45, 105), Point(55, 105))  # set endpoints
        eye2.setWidth(3)
        eye2.draw(win)

        mouth = Oval(Point(30, 90), Point(50, 85))  # set corners of bounding box
        mouth.setFill("red")
        mouth.draw(win)

        label = Text(Point(100, 120), 'A face')
        label.draw(win)

        message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
        message.draw(win)
        win.getMouse()
        win.close()

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
