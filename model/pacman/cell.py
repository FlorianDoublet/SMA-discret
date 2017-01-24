from model.core.agent import Agent
from model.core.Direction import Direction
from model.pacman.agents.wall import Wall
import model.pacman
import random

class Cell(Agent):

	def __init__(self, x, y, environnement):
		self.color = ""
		self.x = x
		self.y = y
		self.environnement = environnement
		self.previous_x = None
		self.previous_y = None
		self.direction = Direction()  # without parameter it's a random direction
		self.old_dir = self.direction
		self.is_trace = False
		self.max = 9999


		self.list_neighbor = []
		self.val = self.max
		self.is_visited = False

	def build_neighbor(self):
		directions = Direction().possible_combination
		for dir in directions:
			x, y = Direction(dir[0], dir[1]).iterate(self.x, self.y)
			col = self.environnement.is_their_a_collision(x, y)
			if not (isinstance(col, tuple) or isinstance(col, Wall)):
				self.list_neighbor.append(self.environnement.grille_dijkstra_val[y][x])

	def is_first(self):
		self.val = 0

	def calculus_dijkstra(self, unvisited_dict):
		"""
		:return: unvisited neighbor
		"""
		self.is_visited = True
		new_val = self.val + 1
		for neigh in self.list_neighbor:
			if not neigh.is_visited:
				unvisited_dict[neigh] = True
				if neigh.val > new_val:
					neigh.val = new_val

	def reset_neigh(self, unvisited_dict):
		self.is_visited = False
		self.val = self.max
		for neigh in self.list_neighbor:
			if neigh.is_visited:
				unvisited_dict[neigh] = True

	def get_nearest_neigh(self):
		val = self.max
		nearest_neigh = None
		random.shuffle(self.list_neighbor)
		for neigh in self.list_neighbor:
			col = self.environnement.is_their_a_collision(neigh.x, neigh.y)
			if (not isinstance(col, Agent)) or isinstance(col, model.pacman.agents.avatar.Avatar):
				if neigh.val < val:
					nearest_neigh = neigh
					val = neigh.val
		return nearest_neigh

	def get_furthest_neigh(self):
		val = 0
		nearest_neigh = None
		random.shuffle(self.list_neighbor)
		for neigh in self.list_neighbor:
			col = self.environnement.is_their_a_collision(neigh.x, neigh.y)
			if (not isinstance(col, Agent)) or isinstance(col, model.pacman.agents.avatar.Avatar):
				if neigh.val > val:
					nearest_neigh = neigh
					val = neigh.val
		return nearest_neigh







