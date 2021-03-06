#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.core.agent import Agent
from utils.PropertiesReader import PropertiesReader


class Particle(Agent):

    def __init__(self, color, x, y, environnement):
        super().__init__(color, x, y, environnement, False)

    def update(self):
        """
        met a jour la position de l'agents sur la carte
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
            if isinstance(collision, Agent):
                agent_col = collision
                # Si la collision est un Agent, alors on inverse les directions des deux agents
                # et on n'update pas ( on avance pas )
                self.old_dir = self.direction
                tmp_dir = agent_col.direction
                agent_col.old_direction = agent_col.direction
                agent_col.direction = self.direction
                self.direction = tmp_dir
                if PropertiesReader.prop.trace():
                    self.print_cvs_change("agents-col")
                    agent_col.print_cvs_change("agents-col")
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

    def next_position(self):
        """
        donne la prochaine position selon la direction de la particule
        :return: x, y qui correspondent a la position
        """
        x, y = self.direction.iterate(self.x, self.y)

        x, y = self.calculate_torrique_position(x, y)

        return x, y

    def wall_collision(self, wall_inv):
        # on inverse l'axe x et ou y selon les valeurs du tuple --> [0] = x_axis, [1] = y_axis
        if wall_inv[0]:
            self.direction.inverse_x_axis()
        if wall_inv[1]:
            self.direction.inverse_y_axis()
        if PropertiesReader.prop.trace():
            self.print_direct_change("wall-col")

    def print_cvs_change(self, cause):
        print("Particle;before;" + self.old_dir.to_string() + ";after;" + self.direction.to_string() + ";at;x;"+str(self.x) + ";y;"+str(self.y)+";cause;"+cause)



