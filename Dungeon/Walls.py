"""This is a class for walls"""
import pygame
from pygame.locals import *

class Walls(pygame.sprite.Sprite):
    def __init__(self, x_index, y_index):
        pygame.sprite.Sprite.__init__(self)

