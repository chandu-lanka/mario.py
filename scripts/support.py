import pygame
from os import walk

def import_folder(path):
    surface_list = []
    for _, __, img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)

    return surface_list