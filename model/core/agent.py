#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc

from model.core.Direction import Direction
from utils.PropertiesReader import PropertiesReader


class Agent:
    __metaclass__ = abc.ABCMeta

    def __init__(self, color, x, y, environnement, is_trace):
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
        self.is_trace = is_trace

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

    @abc.abstractmethod
    def wall_collision(self, wall_inv):
        pass

    @abc.abstractmethod
    def next_position(self):
        pass

    def die(self):
        self.environnement.get_grille()[self.y][self.x] = None
        if self in self.environnement.SMA.agent_list:
            self.environnement.SMA.agent_list.remove(self)

    def calculate_torrique_position(self, x, y):
        if self.environnement.is_torrique:
            y_max = self.environnement.h - 1
            x_max = self.environnement.w - 1
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
    def print_cvs_change(self, cause):
        pass


