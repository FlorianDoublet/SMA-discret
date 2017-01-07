
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
        self.grille2d[agent.y][agent.x] = None


    def is_their_a_collision(self, x, y):
        """
        Methode pour voir si il y a une quelquonque collision
        :param agent:
        :param x: prochaine position x de l'agent
        :param y: prochaine position y de l'agent
        :return: un agent percute, soit un mur traverse, soit rien
        """
        potential_agent = self.grille2d[y][x]
        if potential_agent:
            # si il y a collision avec un autre agent, on renvois cet agent
            return potential_agent

        if y < 0 or x < 0 or x > self.w-1 or y > self.h-1:
            # si il y a collision avec un mur
            return self.wall_collision_direction(x, y, self.w-1, self.h-1)

    @staticmethod
    def wall_collision_direction(x, y, max_x, max_y):
        """

        :param x: prochaine position x de l'agent
        :param y: prochaine position y de l'agent
        :param max_x: borne max de x
        :param max_y: borne max de y
        :return: la "position" ou "direction" (on peux le voir comme on veux) du mur percute ou traverse
        """
        if y < 0 and x < 0:
            return ["up", "left"]
        if y > max_y and x < 0:
            return ["down", "left"]
        if y < 0 and x > max_x:
            return ["up", "right"]
        if y > max_y and x > max_x:
            return ["down", "right"]
        if y < 0:
            return "up"
        if y > max_y:
            return "down"
        if x < 0:
            return "right"
        if x > max_x:
            return "left"











