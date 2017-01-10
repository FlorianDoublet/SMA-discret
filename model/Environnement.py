#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Environnement:

    def __init__(self, w, h, SMA, is_torrique):
        self.w = w
        self.h = h
        self.grille2d = [[None for x in range(self.w)] for y in range(self.h)]
        self.SMA = SMA
        self.is_torrique = is_torrique

    def set_agent(self, agent):
        self.grille2d[agent.y][agent.x] = agent


    def delete_agent(self, agent):
        self.grille2d[agent.previous_y][agent.previous_x] = None

    def get_grille(self):
        return self.grille2d

    def is_their_a_collision(self, x, y):
        """
        Methode pour voir si il y a une quelquonque collision
        :param agent:
        :param x: prochaine position x de l'agent
        :param y: prochaine position y de l'agent
        :return: un agent percute, soit un mur traverse, soit rien
        """

        if y < 0 or x < 0 or x > self.w-1 or y > self.h-1:
            # si il y a collision avec un mur
            return self.wall_collision_direction(x, y, self.w-1, self.h-1)

        potential_agent = self.grille2d[y][x]
        if potential_agent:
            # si il y a collision avec un autre agent, on renvois cet agent
            return potential_agent

    @staticmethod
    def wall_collision_direction(x, y, max_x, max_y):
        """

        :param x: prochaine position x de l'agent
        :param y: prochaine position y de l'agent
        :param max_x: borne max de x
        :param max_y: borne max de y
        :return: un tuple de boolean pour dire quels axes on inverse (x, y, ou les deux)
        """

        inverse_x_dir = False
        inverse_y_dir = False
        if y < 0 or y > max_y:
            # murhautbas
            inverse_y_dir = True
        if x < 0 or x > max_x:
            # murscote
            inverse_x_dir = True

        return (inverse_x_dir, inverse_y_dir)











