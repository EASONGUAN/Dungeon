import pygame
from pygame.locals import *


class magicball(pygame.sprite.Sprite):

    def __init__(self, position, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/magicball.png').convert_alpha()
        self.active = True
        self.speed = 6
        self.direction = ''
        self.damage = 10
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = direction

    def move(self):
        # Can be done by dict and command. Need to improve.
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.active = False
        elif self.direction == 'D':
            if self.rect.bottom < 480:
                self.rect.bottom += self.speed
            else:
                self.active = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.active = False
        elif self.direction == 'R':
            if self.rect.right < 480:
                self.rect.right += self.speed
            else:
                self.active = False

