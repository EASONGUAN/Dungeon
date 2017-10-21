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
        self.root = RootTypeOne(x_index, y_index)

class RootTypeOne(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index + 20
        self.y_index = y_index + 51
        self.init_image = pygame.image.load('images/tree1root.png').convert_alpha()
        self.width = 19
        self.height = 19
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = (x_index + 20), (y_index + 51)
        self.mask = pygame.mask.from_surface(self.init_image)



class TreeTypeTwo(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index
        self.y_index = y_index
        self.init_image = pygame.image.load('images/tree2.png').convert_alpha()
        self.width = 62
        self.height = 62
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = x_index, y_index
        self.mask = pygame.mask.from_surface(self.init_image)
        self.root = RootTypeTwo(x_index, y_index)

class RootTypeTwo(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index + 18
        self.y_index = y_index + 50
        self.init_image = pygame.image.load('images/tree2root.png').convert_alpha()
        self.width = 25
        self.height = 12
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = (x_index + 18), (y_index + 50)
        self.mask = pygame.mask.from_surface(self.init_image)

class StoneTypeOne(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index
        self.y_index = y_index
        self.init_image = pygame.image.load('images/stone.png').convert_alpha()
        self.width = 33
        self.height = 30
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = x_index, y_index
        self.mask = pygame.mask.from_surface(self.init_image)
        self.root = StoneRootTypeOne(x_index, y_index)

class StoneRootTypeOne(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)
        self.x_index = x_index
        self.y_index = y_index + 5
        self.init_image = pygame.image.load('images/stone_root.png').convert_alpha()
        self.width = 33
        self.height = 25
        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = (x_index), (y_index + 5)
        self.mask = pygame.mask.from_surface(self.init_image)