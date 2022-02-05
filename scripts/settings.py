import pygame
from pygame.locals import *

level_map = [
'                                ',
'                                ',
'                                ',
'XX                     XXXXX    ',
'XXX    P                XXXX    ',
'XXXX        XXXX    XX   XXX    ',
'XXXXX                           ',
'       X       XXXXXXXXXXXXX    ',
'      XX        XXXXXXXXXXX     ',
'    XXXX         XXXXXXXXX      ',
'XXXXXXXX          XXXXXXX       ',]

tile_size = 64
WINDOW_SIZE = (1200, len(level_map) * 64)
clock = pygame.time.Clock()