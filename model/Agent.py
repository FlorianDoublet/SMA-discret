#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange

from model.Direction import Direction


class Agent:

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

    def update(self):
        """
        met a jour la position de l'agent sur la carte
        :return:
        """
        self.reset_old_position_in_env()
        self.environnement.set_agent(self)

    def decide(self):
        """
        decide quoi faire pour le mouvement de la particule (si elle se contente d'avancer ou non en cas de collision)
        :return:
        """

        # la prochain position selon la direction
        x, y = self.next_position()


        collision = self.environnement.is_their_a_collision(x, y)

        if collision:
            # si il y a une collision
            if type(collision) is Agent:
                agent_col = collision
                # Si la collision est un Agent, alors on inverse les directions des deux agents
                # et on n'update pas ( on avance pas )
                tmp_dir = agent_col.direction
                agent_col.direction = self.direction
                self.direction = tmp_dir
                return

            elif type(collision) is tuple:
                # Si c'est une string ou une list alors c'est une collision avec un mur
                self.wall_collision(collision)
                return
        else:
            # their is no collision so we can update the position of our Agent
            self.save_previous_pos()
            self.x = x
            self.y = y
            self.update()

    def wall_collision(self, wall_inv):
        # on inverse l'axe x et ou y selon les valeurs du tuple --> [0] = x_axis, [1] = y_axis
        if wall_inv[0]:
            self.direction.inverse_x_axis()
        if wall_inv[1]:
            self.direction.inverse_y_axis()


    def random_direction(self):
        """
        choisit une direction random parmis le voisinage de Moore
        :return:
        """
        direction_size = len(self._directions)
        return self._directions[randrange(direction_size)]

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


