#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from model.pacman.pacman import Pacman
from time import sleep
from utils.PropertiesReader import PropertiesReader


class Main:

    def __init__(self):

        PropertiesReader()
        prop = PropertiesReader.prop
        delay = self.millis_to_sec(prop.delay_ms())
        tick = prop.nb_tick()

        sma = Pacman()
        s = __import__(prop.view(), globals(), locals(), ['*'])
        vue = s.Vue()
        sma.register(vue)


        i = 0
        while i <= tick:
            sma.run()
            sleep(delay)
            if tick > 0:
                i += 1

    def millis_to_sec(self, millis):
        return (millis/1000) % 60

if __name__ == '__main__':
    Main()