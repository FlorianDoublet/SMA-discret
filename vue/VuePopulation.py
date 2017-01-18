from observerPattern.observer import Observer
from utils.PropertiesReader import PropertiesReader
import matplotlib.pyplot as plt


class VuePopulation(Observer):

    def __init__(self):
        self.prop = PropertiesReader.prop
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ys = {}
        self.xs = []
        self.ysFish = []
        self.ysSharks = []
        self.counter = 0
        plt.get_current_fig_manager().window.wm_geometry("+600+50")
        plt.ylabel('Populations')
        plt.ylabel('Ticks')
        self.subCount = 0

    def pop_first_element(self):
            self.subCount = 0
            if len(self.xs) > 100:
                for key, value in self.ys.items():
                    value.pop(0)
                self.xs.pop(0)

    def update(self, *args, **kwargs):

        if self.subCount > 10:
            self.subCount = 0

            self.pop_first_element()

            env = args[0]
            agents = env.SMA.agent_list

            self.xs.append(self.counter)

            types, numbers_of_each_types = self.list_types(agents)

            self.ax1.clear()
            self.draw_plots(types, numbers_of_each_types)

            self.counter += 1
            self.fig.show()
            self.fig.canvas.draw()
        else:
            self.subCount += 1

    def draw_plots(self, types, numbers_of_each_types):
        for t, n in zip(types, numbers_of_each_types):
            if t.__name__ not in self.ys:
                self.ys[t.__name__] = []
            self.ys[t.__name__].append(n)
            self.ax1.plot(self.xs, self.ys[t.__name__], label=str(t.__name__))

    def list_types(self, agents):
        types = []
        numbers_of_each_types = []

        for a in agents:
            t = type(a)
            if t not in types:
                types.append(t)
                numbers_of_each_types.append(0)

            numbers_of_each_types[types.index(t)] += 1

        return types, numbers_of_each_types

    def end_draw(self):
        pass