#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.core.Environnement import Environnement
from model.pacman.cell import Cell


class PacmanEnv(Environnement):

    def __init__(self, w, h, SMA):
        super().__init__(w, h, SMA)
        self.grille_dijkstra_val = [[Cell(x, y, self) for x in range(self.w)] for y in range(self.h)]
        for y in range(self.h):
            for x in range(self.w):
                self.grille_dijkstra_val[y][x].build_neighbor()

    def print_grille_dijkstra(self):
        print("\n")
        for y in range(self.h):
            print(".")
            for x in range(self.w):
                print("|" + str(self.grille_dijkstra_val[y][x].val) + "|", end='')

