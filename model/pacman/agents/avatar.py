from model.core.agent import Agent
from model.pacman.agents.defender import Defender
from model.pacman.agents.hunter import Hunter
from model.pacman.agents.wall import Wall
from model.pacman.agents.winner import Winner

from pynput import keyboard


class Avatar(Agent):

    def __init__(self, color, x, y, environnement, is_trace):
        super().__init__(color, x, y, environnement, is_trace)
        self.nb_defender_eaten = 0

        self.listener = keyboard.Listener(
                on_press=self.on_press)

        self.listener.start()

    def on_press(self, key):
        if key == keyboard.Key.up:
            self.direction.y_axis = -1
            self.direction.x_axis = 0
        if key == keyboard.Key.down:
            self.direction.y_axis = 1
            self.direction.x_axis = 0
        if key == keyboard.Key.left:
            self.direction.y_axis = 0
            self.direction.x_axis = -1
        if key == keyboard.Key.right:
            self.direction.y_axis = 0
            self.direction.x_axis = 1

    def update(self):
        self.reset_old_position_in_env()
        self.environnement.set_agent(self)

    def decide(self):
        x, y = self.next_position()
        collision = self.environnement.is_their_a_collision(x, y)
        if isinstance(collision, Agent):
            self.decide_by_agent(collision, x, y)
        elif type(collision) is tuple:
            pass
        else:
            self.save_previous_pos()
            self.x = x
            self.y = y
            self.update()

        self.direction.y_axis = 0
        self.direction.x_axis = 0

    def decide_by_agent(self, agent, x, y):
        if type(agent) is Wall:
            # don't move :)
            pass
        elif type(agent) is Defender:
            agent.die()
            self.nb_defender_eaten += 1
            # todo
            # if nb_defender_eaten ... then winner created

            self.save_previous_pos()
            self.x = x
            self.y = y
            self.update()
            self.environnement.SMA.create_new_defender()
        elif type(agent) is Hunter:
            self.die() # FIN DU GAME
            pass
        elif type(agent) is Winner:
            # todo --> on gagne :D
            pass

    def die(self):
        # todo --> exit le game
        pass

    def wall_collision(self, wall_inv):
        pass

    def next_position(self):
        x, y = self.direction.iterate(self.x, self.y)

        x, y = self.calculate_torrique_position(x, y)

        return x, y

    def print_cvs_change(self, cause):
        pass