import json

class Projector():
	"""A basic attempt to model a data projector"""
	def __init__(self, display_standard, output, noise=10, lenses={}):
		self.display_standard = display_standard
		self.output = output
		self.noise = noise
		self.lenses = lenses

	def get_projector_resolution(self):
		"""Look up projector against JSON file of display standards"""
		with open('display_standards.json') as json_file:
			display_standards_dict = json.load(json_file)

		# extract list of dicts from dict
		display_standards = display_standards_dict['display_standards']
		
		# look for match in standards list
		standard = next(
			item for item in display_standards if
			item["standard"] == self.display_standard
			)

		# set up some variables
		pixel_width = standard['width']
		pixel_height = standard['height']
		pixel_count = pixel_width * pixel_height

		# print the resolution specs
		print(
			"This is an " + self.display_standard.upper() + 
			" projector, meaning it produces an image of " +
			str(pixel_width) + "px wide and " + str(pixel_height) + "px high.")
		print("Total pixel count: " + str(pixel_count) + ".")
