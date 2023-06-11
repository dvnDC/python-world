from .plant import Plant
from position import Position
from action import Action
from action_enum import ActionEnum


class Toadstool(Plant):

	def __init__(self, toadstool=None, position=None, world=None):
		super(Toadstool, self).__init__(toadstool, position, world)
		self.__color = (255, 0, 0)  # Add the color attribute, for example, red color (R, G, B)

	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	def clone(self):
		return Toadstool(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 0
		self.liveLength = 10
		self.powerToReproduce = 5
		self.sign = 'T'

	def consequences(self, atackingOrganism):
		result = []

		if self.power > atackingOrganism.power:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		else:
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, self))
			result.append(Action(ActionEnum.A_REMOVE, Position(xPosition=-1, yPosition=-1), 0, atackingOrganism))
		return result
