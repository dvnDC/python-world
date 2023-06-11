import pygame
from pygame.locals import *
from Organisms.colors import Colors


def init_screen(resolution=(800, 600)):
    pygame.init()
    screen = pygame.display.set_mode(resolution)
    pygame.display.set_caption('My World Simulation')
    return screen

def draw_world(screen, world):
    screen.fill((0, 0, 0))  # Fill the screen with white color

    for organism in world.organisms:
        x, y = organism.position.x, organism.position.y
        color = organism.color  # Assuming each organism has a color attribute
        color = Colors.ORGANISM_COLORS[organism.__class__.__name__]  # Pobierz kolor dla danego organizmu

        pygame.draw.circle(screen, color, (x * 50 + 25, y * 50 + 25), 20)

    pygame.display.flip()  # Update the display
