from model.core.agent import Agent
from model.pacman.agents.defender import Defender
from model.pacman.agents.hunter import Hunter
from model.pacman.agents.wall import Wall
from model.pacman.agents.winner import Winner


class Avatar(Agent):

    def __init__(self, color, x, y, environnement, is_trace):
        super().__init__(color, x, y, environnement, is_trace)
        self.nb_defender_eaten = 0

    def update(self):
        self.reset_old_position_in_env()
        self.environnement.set_agent(self)

    def decide(self):
        x, y = self.next_position()
        collision = self.environnement.is_their_a_collision(x, y)
        if collision is Agent:
            self.decide_by_agent(collision)
        else:
            self.update()


    def decide_by_agent(self, agent):
        if agent is Wall:
            # don't move :)
            pass
        elif agent is Defender:
            agent.die()
            self.nb_defender_eaten += 1
            # todo
            # if nb_defender_eaten ... then winner created
            self.update()
        elif agent is Hunter:
            self.die() # FIN DU GAME
            pass
        elif agent is Winner:
            # todo --> on gagne :D
            pass

    def die(self):
        # todo --> exit le game
        pass


    def wall_collision(self, wall_inv):
        pass

    def next_position(self):
        return 17, 17


    def print_cvs_change(self, cause):
        pass