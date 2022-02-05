import pygame
from scripts.tile import Tile
import scripts.settings

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.draw_level(level_data)

    def draw_level(self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == 'X':
                    x = col_index * scripts.settings.tile_size
                    y = row_index * scripts.settings.tile_size
                    tile = Tile((x,y), scripts.settings.tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(-1)
        self.tiles.draw(self.display_surface)