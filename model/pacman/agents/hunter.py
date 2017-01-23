from model.core.agent import Agent
import model.pacman


class Hunter(Agent):

    def __init__(self, color, x, y, environnement, is_trace):
        super().__init__(color, x, y, environnement, is_trace)

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

    def decide_by_agent(self, agent, x, y):
        if type(agent) is model.pacman.agents.avatar.Avatar:
            if agent.current_invincibility > agent.invincibility_time:
                agent.die()
            pass

    def next_position(self):
        x, y = self.direction.random_dir()
        x += self.x
        y += self.y

        x, y = self.calculate_torrique_position(x, y)

        return x, y
