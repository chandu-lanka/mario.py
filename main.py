import pygame
from pygame.locals import *
import scripts.settings
from scripts.level import Level
import sys

pygame.init()
screen = pygame.display.set_mode(scripts.settings.WINDOW_SIZE)
pygame.display.set_caption("mario")
lvl = Level(scripts.settings.level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 200, 125))
    lvl.run()

    pygame.display.update()
    scripts.settings.clock.tick(60)