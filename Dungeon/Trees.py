"""This is a class for Trees"""
import pygame
from pygame.locals import *

class TreeTypeOne(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index
        self.y_index = y_index
        self.init_image = pygame.image.load('images/tree1.png').convert_alpha()
        self.width = 58
        self.height = 81
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = x_index, y_index
        self.mask = pygame.mask.from_surface(self.init_image)
        #self.root = RootTypeOne(x_index, y_index)

class RootTypeOne(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index + 9
        self.y_index = y_index + 41
        self.init_image = pygame.image.load('images/empty_root.png').convert_alpha()
        self.width = 40
        self.height = 40
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = (x_index + 9), (y_index + 41)
        self.mask = pygame.mask.from_surface(self.init_image)
