import pygame
from entities.mario import Mario
from scripts.tile import Tile
import scripts.settings

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.draw_level(level_data)
        self.world_shift = 0

    def draw_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.mario = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * scripts.settings.tile_size    
                y = row_index * scripts.settings.tile_size

                if cell == 'X':
                    tile = Tile((x,y), scripts.settings.tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    mario_sprite = Mario((x,y))
                    self.mario.add(mario_sprite)

    def scroll_x_axis(self):
        mario = self.mario.sprite
        mario_x = mario.rect.centerx
        dir_x = mario.direction.x

        if mario_x < scripts.settings.WINDOW_SIZE[0] /4 and dir_x < 0:
            self.world_shift = 5
            mario.speed = 0
        elif mario_x > scripts.settings.WINDOW_SIZE[0] - (scripts.settings.WINDOW_SIZE[0] / 4) and dir_x > 0:
            self.world_shift = -5
            mario.speed = 0
        else:
            self.world_shift = 0
            mario.speed = 5

    def horizontal_movement_col(self):
        mario = self.mario.sprite
        mario.rect.x += mario.direction.x * mario.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(mario.rect):
                if mario.direction.x < 0:
                    mario.rect.left = sprite.rect.right
                elif mario.direction.x > 0:
                    mario.rect.right = sprite.rect.left

    def vertical_movement_col(self):
        mario = self.mario.sprite
        mario.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(mario.rect):
                if mario.direction.y > 0:
                    mario.rect.bottom = sprite.rect.top
                    mario.direction.y = 0
                elif mario.direction.y < 0:
                    mario.rect.top = sprite.rect.bottom
                    mario.direction.y = 0

    def run(self):
        #tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        
        #player
        self.mario.draw(self.display_surface)
        self.mario.update()
        self.scroll_x_axis()
        self.horizontal_movement_col()
        self.vertical_movement_col()