#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.SMA import SMA
from vue.Vue import Vue
from time import sleep


class Main:

    def __init__(self):
        w = 20
        h = 20
        n = 5
        box_size = 10

        sma = SMA(w, h, n)
        vue = Vue(w, h, box_size)

        sma.register(vue)

        while(True):
            sma.run()
            sleep(0.2)

        vue.end_draw()


if __name__ == '__main__':
    Main()