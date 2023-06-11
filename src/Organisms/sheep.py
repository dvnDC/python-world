from .animal import Animal


class Sheep(Animal):

	def __init__(self, sheep=None, position=None, world=None):
		super(Sheep, self).__init__(sheep, position, world)
		self.__color = (255, 0, 0)  # Add the color attribute, for example, red color (R, G, B)

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	def clone(self):
		return Sheep(self, None, None)

	def initParams(self):
		self.power = 3
		self.initiative = 3
		self.liveLength = 10
		self.powerToReproduce = 6
		self.sign = 'S'

	def getNeighboringPositions(self):
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))
