import pygame
from scripts.support import import_folder

class Mario(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_sprites()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = pygame.Surface((32, 32))
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        
        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.gravity = 0.8
        self.jump_speed = -16

    def import_sprites(self):
        sprite_path = './data/sprites/mario/'
        self.animations = {'idle': [], 'run': [], 'jump': []}

        for animation in self.animations.keys():
            full_path = sprite_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations['idle']

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.animate()