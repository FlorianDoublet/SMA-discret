from observerPattern.observer import Observer
from utils.PropertiesReader import PropertiesReader
from model.wator import Fish, Shark
import matplotlib.pyplot as plt


class VueRatio(Observer):

    def __init__(self):
        self.prop = PropertiesReader.prop
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ys = []
        self.xs = []
        self.counter = 0
        plt.get_current_fig_manager().window.wm_geometry("+600+50")
        plt.ylabel('Populations')
        plt.ylabel('Ticks')
        self.subCount = 0

    def pop_first_element(self):
            self.subCount = 0
            if len(self.xs) > 100:
                self.ys.pop(0)
                self.xs.pop(0)

    def update(self, *args, **kwargs):

        if self.subCount > 10:
            self.subCount = 0

            self.pop_first_element()

            env = args[0]
            agents = env.SMA.agent_list



            nb_fish, nb_shark = self.num_fish_on_shark(agents)
            self.xs.append(nb_fish)

            self.ax1.clear()
            self.draw_plots(nb_shark)

            self.counter += 1
            self.fig.show()
            self.fig.canvas.draw()
        else:
            self.subCount += 1

    def draw_plots(self, nb_shark):
            self.ys.append(nb_shark)
            self.ax1.plot(self.xs, self.ys, label=str("num fish on shark"))

    def num_fish_on_shark(self, agent_list):
        fish = 0
        shark = 0
        for agent in agent_list:
            if isinstance(agent, Fish.Fish):
                fish += 1
            else:
                shark += 1
        return fish, shark

    def end_draw(self):
        pass