#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange
from itertools import *


class Direction:

    def __init__(self, x_axis=None, y_axis=None):
        if x_axis and y_axis:
            self.x_axis = x_axis
            self.y_axis = y_axis
        else:
            self.x_axis, self.y_axis = self.random_dir()

    def iterate(self, x, y):
        y += self.y_axis
        x += self.x_axis
        return x, y

    @staticmethod
    def random_dir():
        values = [0, 1, -1]
        possible_combination = []
        for val in combinations_with_replacement(values, 2):
            if val != (0, 0):
                possible_combination.append(val)

        tirage = possible_combination[randrange(len(possible_combination))]
        return tirage[0], tirage[1]

    def inverse_x_axis(self):
        self.x_axis *= -1

    def inverse_y_axis(self):
        self.y_axis *= -1
