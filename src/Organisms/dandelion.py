from .plant import Plant


class Dandelion(Plant):

	def __init__(self, dandelion=None, position=None, world=None):
		super(Dandelion, self).__init__(dandelion, position, world)
		self.__color = (255, 0, 0)  # Add the color attribute, for example, red color (R, G, B)

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	def clone(self):
		return Dandelion(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 0
		self.liveLength = 6
		self.powerToReproduce = 2
		self.sign = 'D'
