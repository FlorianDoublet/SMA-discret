from model.wator.reproductible_creature import ReproductibleCreature
from .Fish import Fish
from itertools import product
from random import randrange


class Shark(ReproductibleCreature):
    def __init__(self, breed_time, color, x, y, env):
        super().__init__(breed_time, color, x, y, env)
        self.shark_starve_time = 8
        self.last_time_he_ate = 0 # Compteur pour famine

    def update(self):
        self.reset_old_position_in_env()
        self.reproduce(self.previous_x, self.previous_y) # Se reproduit juste avant de bouger
        self.environnement.set_agent(self)

    def reproduce(self, x, y):
        if self.age > self.breed_time:
            baby = Shark(self.breed_time, "pink", x, y, self.environnement)
            self.environnement.SMA.agent_list.append(baby)
            self.environnement.set_agent(baby)
        pass

    def decide(self):
        x, y = self.next_position()

        collision = self.environnement.is_their_a_collision(x, y)

        if collision:
            if isinstance(collision, Fish): # Miam miam
                collision.die() # Onomnomnomnom
                self.last_time_he_ate = 0 # N'a plus faim :)
                self.save_previous_pos()
                self.x = x
                self.y = y
                self.update()
        else:
            self.save_previous_pos()
            self.x = x
            self.y = y
            self.update()

            self.age += 1  # Prend de l'age
            if self.last_time_he_ate >= self.shark_starve_time:
                self.die()  # Meurs de faim
            else:
                self.last_time_he_ate += 1

    def detect_fishes(self):
        """
        Detecte les poissons autours
        :return:
        """
        near_fishes = []

        possible_combination = [i for i in product(range(-1, 2), repeat=2)]
        possible_combination.remove((0, 0))
        for x, y in possible_combination:
            x = self.x+x
            y = self.y+y
            x, y = self.calculate_torrique_position(x, y)
            element = self.environnement.is_their_a_collision(x, y)
            if element is Fish:
                near_fishes.append(element)

        return near_fishes

    def next_position(self):
        """
        Si y'a des poisssons autours, il va en cibler un au hasard
        Si y'a pas de poisson il fait rien
        :return:
        """
        near_fishes = self.detect_fishes()

        if not near_fishes:
            x, y = self.direction.random_dir()
            x = self.x + x
            y = self.y + y
            x, y = self.calculate_torrique_position(x, y)
            return x, y
        else:
            n = randrange(0, len(near_fishes))
            x = near_fishes[n].x
            y = near_fishes[n].y
            return x, y

    def wall_collision(self, wall_inv):
        pass

    def print_direct_change(self, cause):
        pass
