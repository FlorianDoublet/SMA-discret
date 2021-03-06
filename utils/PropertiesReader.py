#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from pathlib import Path


class PropertiesReader:
	prop = None

	def __init__(self):

		my_file = Path("utils/properties.json")
		if not my_file.is_file():
			my_file = Path("../../utils/properties.json")

		with my_file.open() as json_data:
			self.properties = json.load(json_data)
		self.general_param = self.properties["general_parameter"]
		self.specific_param = self.properties["specific_parameter"]
		self.wator = self.properties["wator"]
		self.pacman = self.properties["pacman"]
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

	def canvas_background_color(self):
		return self.specific_param["canvas_background_color"]

	def grid_color(self):
		return self.specific_param["grid_color"]

	def random_mix_color(self):
		if self.specific_param["random_mix_color"][0]:
			string_color = self.specific_param["random_mix_color"][1]
			string_color = string_color.split(",")
			return (int(string_color[0]), int(string_color[1]), int(string_color[2]))
		else:
			return False

	def view(self):
		views = self.specific_param["view"]
		for view in views:
			for key, val in view.items():
				if val:
					view_import = ""
					if key == "tkinter":
						view_import = "vue.VueTkinter"
					elif key == "pygame":
						view_import = "vue.VuePyGame"
					return view_import

	def fish(self):
		return self.wator["fish"]

	def shark(self):
		return self.wator["shark"]

	def nb_fish(self):
		return self.fish()["nb"]

	def nb_shark(self):
		return self.shark()["nb"]

	def breed_time_fish(self):
		return self.fish()["breed_time"]

	def breed_time_shark(self):
		return self.shark()["breed_time"]

	def starve_time_shark(self):
		return self.shark()["starve_time"]

	def wall_percent(self):
		return self.pacman["wall"]["percent"]

	def nb_hunter(self):
		return self.pacman["hunter"]["nb"]

	def speed_hunter(self):
		return self.pacman["hunter"]["speed"]

	def speed_avatar(self):
		return self.pacman["avatar"]["speed"]
