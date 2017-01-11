#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

from model.core.Direction import Direction
from utils.PropertiesReader import PropertiesReader


class Agent:
    __metaclass__ = abc.ABCMeta

    def __init__(self, color, x, y, environnement):

        self.color = color
        self.x = x
        self.y = y
        self.environnement = environnement
        # un agent s'ajoute lui meme dans l'environnement dans l'initialisation
        self.environnement.set_agent(self)
        self.previous_x = None
        self.previous_y = None
        self.direction = Direction()  # without parameter it's a random direction
        self.old_dir = self.direction

    @abc.abstractmethod
    def update(self):
        """
        met a jour la position de l'agent sur la carte
        :return:
        """
        pass

    @abc.abstractmethod
    def decide(self):
        """
        decide quoi faire pour le mouvement de la particule (si elle se contente d'avancer ou non en cas de collision)
        :return:
        """
        pass

    def wall_collision(self, wall_inv):
        # on inverse l'axe x et ou y selon les valeurs du tuple --> [0] = x_axis, [1] = y_axis
        if wall_inv[0]:
            self.direction.inverse_x_axis()
        if wall_inv[1]:
            self.direction.inverse_y_axis()
        if PropertiesReader.prop.trace():
            self.print_direct_change("wall-col")



    def next_position(self):
        """
        donne la prochaine position selon la direction de la particule
        :return: x, y qui correspondent a la position
        """
        x, y = self.direction.iterate(self.x, self.y)

        if self.environnement.is_torrique:
            y_max = self.environnement.h-1
            x_max = self.environnement.w-1
            # si on peux passer a travers les murs alors on calcul la position en fonction de ce parametre
            if y < 0:
                y = y_max
            elif y > y_max:
                y = 0

            if x < 0:
                x = x_max
            elif x > x_max:
                x = 0

        return x, y

    def save_previous_pos(self):
        self.previous_x = self.x
        self.previous_y = self.y

    def reset_old_position_in_env(self):
        self.environnement.delete_agent(self)

    @abc.abstractmethod
    def print_direct_change(self, cause):
        pass


