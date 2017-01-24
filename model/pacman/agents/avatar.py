import sys
from model.core.agent import Agent
from model.pacman.agents.defender import Defender
from model.pacman.agents.hunter import Hunter
from model.pacman.agents.wall import Wall
from model.pacman.agents.winner import Winner
from pynput import keyboard
import pynput._util.win32_vks as VK
from model.pacman.dijkstra import Dijkstra
from model.core.Direction import Direction


class Avatar(Agent):

    def __init__(self, color, x, y, environnement, is_trace):
        super().__init__(color, x, y, environnement, is_trace)
        self.nb_defender_eaten = 0
        self.winner_created = False
        self.invincibility_time = 250
        self.current_invincibility = self.invincibility_time
        self.dijkstra = Dijkstra()

        self.listener = keyboard.Listener(on_press=self.on_press)
        self.direction = Direction(0,0)
        self.dijkstra.compute(self.environnement.grille_dijkstra_val[self.y][self.x])
        #self.environnement.print_grille_dijkstra()

        self.listener.start()

    def on_press(self, key):
        if key == keyboard.KeyCode.from_char('8'):
            self.direction.x_axis = 0
            self.direction.y_axis = -1
        if key == keyboard.KeyCode.from_vk(65437): # touche 5 du num pad
            self.direction.x_axis = 0
            self.direction.y_axis = 1
        if key == keyboard.KeyCode.from_char('4'):
            self.direction.x_axis = -1
            self.direction.y_axis = 0
        if key == keyboard.KeyCode.from_char('6'):
            self.direction.x_axis = 1
            self.direction.y_axis = 0

        if key == keyboard.KeyCode.from_char('7'):
            self.direction.y_axis = -1
            self.direction.x_axis = -1
        if key == keyboard.KeyCode.from_char('9'):
            self.direction.y_axis = -1
            self.direction.x_axis = 1
        if key == keyboard.KeyCode.from_char('1'):
            self.direction.y_axis = 1
            self.direction.x_axis = -1
        if key == keyboard.KeyCode.from_char('3'):
            self.direction.y_axis = 1
            self.direction.x_axis = 1

        sma = self.environnement.SMA
        if key == keyboard.KeyCode.from_char('a'):
            if sma.avatar_speed > 1:
                sma.avatar_speed -= 1
        if key == keyboard.KeyCode.from_char('z'):
            sma.avatar_speed += 1
        if key == keyboard.KeyCode.from_char('o'):
            if sma.hunter_speed > 1:
                sma.hunter_speed -= 1
        if key == keyboard.KeyCode.from_char('p'):
            sma.hunter_speed += 1

    def update(self):
        self.dijkstra.reset(self.environnement.grille_dijkstra_val[self.y][self.x])
        self.dijkstra.compute(self.environnement.grille_dijkstra_val[self.y][self.x])
        #self.environnement.print_grille_dijkstra()
        self.reset_old_position_in_env()
        self.environnement.set_agent(self)

    def decide(self):
        sma = self.environnement.SMA
        if (sma.tick % sma.avatar_speed != 0):
            return
        # Gestion invincibilite
        if self.current_invincibility < self.invincibility_time and (self.current_invincibility % 2 == 0):
            self.color = "cyan"
        if self.current_invincibility < self.invincibility_time and (self.current_invincibility % 2 != 0):
            self.color = "yellow"
        if self.current_invincibility > self.invincibility_time:
            self.environnement.is_player_invincible = False
        if self.current_invincibility < self.invincibility_time:
                self.environnement.is_player_invincible = True
        self.current_invincibility += 1

        # Gestion deplacement
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

        #self.direction.y_axis = 0
        #self.direction.x_axis = 0

    def decide_by_agent(self, agent, x, y):
        if type(agent) is Wall:
            # don't move :)
            pass
        elif type(agent) is Defender:
            agent.die()
            self.nb_defender_eaten += 1

            if self.nb_defender_eaten >= 4 and not self.winner_created:
                self.environnement.SMA.create_winner()
                self.winner_created = True

            self.save_previous_pos()
            self.x = x
            self.y = y
            self.update()
            self.environnement.SMA.create_new_defender()

            self.current_invincibility = 0
            self.color = "pink"
        elif type(agent) is Hunter:
            if self.current_invincibility > self.invincibility_time:
                self.die()
            pass
        elif type(agent) is Winner:
            agent.die()
            self.environnement.SMA.is_finish = True
            print('\033[92m' + 'YOU WON !' + '\033[0m')

    def die(self):
        self.environnement.SMA.is_finish = True
        print('\033[91m' + 'YOU LOST !' + '\033[0m')

    def wall_collision(self, wall_inv):
        pass

    def next_position(self):
        x, y = self.direction.iterate(self.x, self.y)

        x, y = self.calculate_torrique_position(x, y)

        return x, y

    def print_cvs_change(self, cause):
        pass

    def build_dijkstra_path(self):
        dij_grid = self.environnement.grille_dijkstra_val

