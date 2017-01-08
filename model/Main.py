from model.SMA import SMA
from vue.Vue import Vue

class Main:

    def __init__(self):
        sma = SMA(300, 300, 500)
        vue = Vue(300, 300)

        sma.register(vue)

        while(True):
            sma.run()

        vue.end_draw()


if __name__ == '__main__':
    Main()