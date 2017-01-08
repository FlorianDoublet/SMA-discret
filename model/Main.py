from model.SMA import SMA
from vue.Vue import Vue

class Main:

    def __init__(self):
        sma = SMA(50, 50, 1)
        vue = Vue(50, 50)

        sma.register(vue)

        while(True):
            sma.run()

        vue.end_draw()


if __name__ == '__main__':
    Main()