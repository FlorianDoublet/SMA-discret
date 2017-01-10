#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.SMA import SMA
from vue.Vue import Vue
from time import sleep
import time


class Main:

    def __init__(self):
        w = 10
        h = 10
        n = 5
        box_size = 80

        sma = SMA(w, h, n)
        vue = Vue(w, h, box_size)

        sma.register(vue)
        i = 0

        start_time = time.time()

        while(i < 3000000):
            sma.run()
            i += 1
            sleep(0.02)

        vue.end_draw()

        print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    Main()