#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange
from itertools import *

class Direction:

    def __init__(self, x_axis=None, y_axis=None):
        self.possible_combination = [i for i in product(range(-1, 2), repeat=2)]
        self.possible_combination.remove((0, 0))
        self.combination_range = len(self.possible_combination)

        if x_axis and y_axis:
            self.x_axis = x_axis
            self.y_axis = y_axis
        else:
            self.x_axis, self.y_axis = self.random_dir()

    def iterate(self, x, y):
        y += self.y_axis
        x += self.x_axis
        return x, y

    def random_dir(self):
        tirage = self.possible_combination[randrange(self.combination_range)]
        return tirage[0], tirage[1]

    def inverse_x_axis(self):
        self.x_axis *= -1

    def inverse_y_axis(self):
        self.y_axis *= -1

    def to_string(self):
        dir = ""
        if self.y_axis == -1:
            dir += "up"
        elif self.y_axis == 1:
            dir += "down"
        elif self.x_axis == -1:
            dir += "left"
        elif self.x_axis == 1:
            dir += "right"
        return dir
