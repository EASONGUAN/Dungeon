import pygame
import time

class SoldierTypeOne(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.count = 0
        self.exp_carried = 50
        self.turn = False
        self.health = 25
        self.attack = 3
        self.world_width = width
        self.world_height = height
        self.init_image = pygame.image.load('images/s1_left.png').convert_alpha()
        self.left_image = pygame.image.load('images/s1_left.png').convert_alpha()
        self.right_image = pygame.image.load('images/s1_right.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.init_image)
        self.left_move_image = []
        self.left_move_image.extend([
            pygame.image.load('images/s1_left.png').convert_alpha(), \
            pygame.image.load('images/s1_left.png').convert_alpha()
        ])

        self.right_move_image = []
        self.right_move_image.extend([
            pygame.image.load('images/s1_right.png').convert_alpha(), \
            pygame.image.load('images/s1_right.png').convert_alpha()
        ])

        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = position[0], position[1]
        self.active = True

    def moveleft(self):
        for index in range(100):
            self.init_image = self.left_move_image[index % 2]
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveright(self):
        for index in range(100):
            self.init_image = self.right_move_image[index % 2]
        if self.rect.right < self.world_width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.world_width

    def move(self):
        if self.count < 50 and self.turn == False:
            self.moveright()
            self.count += 1
        elif self.count < 50 and self.turn == True:
            self.moveleft()
            self.count += 1
        elif self.count == 50:
            self.count = 0
            self.turn = not(self.turn)

class SoldierTypeTwo(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.count = 0
        self.exp_carried = 50
        self.turn = False
        self.health = 25
        self.attack = 3
        self.world_width = width
        self.world_height = height
        self.init_image = pygame.image.load('images/s1_left.png').convert_alpha()
        self.up_image = pygame.image.load('images/s1_left.png').convert_alpha()
        self.down_image = pygame.image.load('images/s1_right.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.init_image)
        self.up_move_image = []
        self.up_move_image.extend([
            pygame.image.load('images/s1_left.png').convert_alpha(), \
            pygame.image.load('images/s1_left.png').convert_alpha()
        ])

        self.down_move_image = []
        self.down_move_image.extend([
            pygame.image.load('images/s1_right.png').convert_alpha(), \
            pygame.image.load('images/s1_right.png').convert_alpha()
        ])

        self.rect = self.init_image.get_rect()
        self.rect.left, self.rect.top = position[0], position[1]
        self.active = True

    def moveup(self):
        for index in range(100):
            self.init_image = self.up_move_image[index % 2]
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def movedown(self):
        for index in range(100):
            self.init_image = self.down_move_image[index % 2]
        if self.rect.bottom < self.world_height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.world_height - 60

    def move(self):
        if self.count < 50 and not self.turn:
            self.moveup()
            self.count += 1
        elif self.count < 50 and self.turn:
            self.movedown()
            self.count += 1
        elif self.count == 50:
            self.count = 0
            self.turn = not(self.turn)








