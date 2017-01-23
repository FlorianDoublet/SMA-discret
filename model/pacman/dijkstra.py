from model.pacman.cell import Cell


class Dijkstra:

	def __init__(self):
		self.unvisited = {}

	def compute(self, first_cell):
		first_cell.is_first()
		first_cell.calculus_dijkstra(self.unvisited)
		for neigh in first_cell.list_neighbor:
			self.unvisited[neigh] = True
		while(len(self.unvisited)):
			unvisited_cpy = self.unvisited.copy()
			for node in unvisited_cpy:
				node.calculus_dijkstra(self.unvisited)
				del self.unvisited[node]


