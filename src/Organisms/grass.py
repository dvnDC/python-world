from .plant import Plant


class Grass(Plant):

	def __init__(self, grass=None, position=None, world=None):
		super(Grass, self).__init__(grass, position, world)
		self.__color = (255, 0, 0)  # Add the color attribute, for example, red color (R, G, B)

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	def clone(self):
		return Grass(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 0
		self.liveLength = 6
		self.powerToReproduce = 3
		self.sign = 'G'
