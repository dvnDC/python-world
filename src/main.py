from world import World
from position import Position
from Organisms.grass import Grass
from Organisms.sheep import Sheep
from Organisms.dandelion import Dandelion
from Organisms.wolf import Wolf
from Organisms.toadstool import Toadstool
from Engine.engine import *
import sys

SCALE = 20
GRID_HORIZONTAL = 50
GRID_VERTICAL = 35

if __name__ == '__main__':
	pyWorld = World(GRID_HORIZONTAL, GRID_VERTICAL)


	newOrg = Grass(position=Position(xPosition=4, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=0, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Dandelion(position=Position(xPosition=0, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Wolf(position=Position(xPosition=7, yPosition=7), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Toadstool(position=Position(xPosition=4, yPosition=4), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	screen = init_screen((GRID_HORIZONTAL * SCALE, GRID_VERTICAL * SCALE))
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		draw_world(screen, pyWorld)
		pyWorld.makeTurn()
		pygame.time.delay(500)
