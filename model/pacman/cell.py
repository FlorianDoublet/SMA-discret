from model.core.agent import Agent
from model.core.Direction import Direction
from model.pacman.agents.wall import Wall

class Cell(Agent):

	def __init__(self, x, y, environnement):
		super().__init__("", x, y, environnement, False)
		self.list_neighbor = []

	def build_neighbor(self):
		directions = Direction().possible_combination
		for dir in directions:
			x, y = Direction(dir[0], dir[1]).iterate(self.x, self.y)
			col = self.environnement.is_their_a_collision(x, y)
			if col is tuple or col is Wall:
				print("coucou")
				self.list_neighbor.append(self.environnement.grille_dijkstra_val[x][y])





