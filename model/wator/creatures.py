from model.core.core import Core
from itertools import product
from model.wator.Fish import Fish
from model.wator.Shark import Shark
import random

class Creatures(Core):

	def __init__(self):
		super().__init__()

	def init_agents(self):
		nb_fish = 45
		nb_shark = 10
		fish_breed = 10
		shark_breed = 5
		shark_starve = 8

		# Generer toutes les permutations possibles
		every_possible_tuple_position = [i for i in product(range(max(self.w, self.h)), repeat=2)]

		index = 0
		if self.h > self.w:
			index = 1

		every_possible_tuple_position = [i for i in every_possible_tuple_position if i[index] < min(self.w, self.h)]

		# Recuperer x valeurs de toutes les permutations possible sans doublons
		positions = random.sample(every_possible_tuple_position, nb_fish + nb_shark)

		# On cree les agents
		self.agent_list = []
		fish_added = 0
		shark_added = 0
		for p in positions:
			if fish_added < nb_fish:
				self.agent_list.append(Fish(fish_breed, "green", p[1], p[0], self.environnement))
				fish_added += 1
			else:
				self.agent_list.append(Shark(shark_breed, "pink", p[1], p[0], self.environnement))
				shark_added += 1

	def print_tick(self):
		print("Tick;" + str(self.tick))

