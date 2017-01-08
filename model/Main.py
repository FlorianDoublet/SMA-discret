from model.SMA import SMA
from vue.Vue import Vue
from time import sleep

class Main:

    def __init__(self):
        sma = SMA(300, 300, 50)
        vue = Vue(300, 300)

        sma.register(vue)

        while(True):
            sma.run()
            sleep(0.02)

        vue.end_draw()


if __name__ == '__main__':
    Main()