#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

class PropertiesReader:

	prop = None

	def __init__(self):

		with open('../utils/properties.json') as json_data:
			self.properties = json.load(json_data)
		self.general_param = self.properties["general_parameter"]
		self.specific_param = self.properties["specific_parameter"]
		PropertiesReader.prop = self

	def print_json(self):
		print(self.properties)

	def grid_size(self):
		grid_size = self.general_param["grid_size"]
		return grid_size["grid_size_x"], grid_size["grid_size_y"]

	def canvas_size(self):
		canvas_size = self.general_param["canvas_size"]
		return canvas_size["canvas_size_x"], canvas_size["canvas_size_y"]

	def box_size(self):
		return self.general_param["box_size"]

	def delay_ms(self):
		return self.general_param["delay_ms"]

	def sheduling(self):
		shedules = self.general_param["sheduling"]
		for shedule in shedules:
			for key, val in shedule.items():
				if val:
					return key

	def nb_tick(self):
		return self.general_param["nb_tick"]

	def print_grid(self):
		return self.general_param["print_grid"]

	def trace(self):
		return self.general_param["trace"]

	def random_seed(self):
		return self.general_param["random_seed"]

	def refresh(self):
		return self.general_param["refresh"]

	def toric(self):
		return self.general_param["toric"]

	def nb_particles(self):
		return self.specific_param["nb_particles"]
