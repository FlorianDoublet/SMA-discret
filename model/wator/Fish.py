from model.wator.reproductible_creature import ReproductibleCreature


class Fish(ReproductibleCreature):

	def __init__(self, breed_time, color, x, y, env):
		super().__init__(breed_time, color, x, y, env)

	def update(self):
		pass

	def decide(self):
		pass

	def print_direct_change(self, cause):
		pass
