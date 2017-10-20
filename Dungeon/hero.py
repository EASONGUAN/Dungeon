import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        pygame.sprite.Sprite.__init__(self)

        #  some main features for hero, such as attack, hp and exp.
        self.level = 1
        self.attack = 2
        self.health = 100
        self.exp = 0
        self.speed = 4
        #  ends here
        # self.explosion_image = pygame.image.load('images/hero_explosion.png').convert_alpha()
        self.world_width = width
        self.world_height = height
        self.init_image = pygame.image.load('images/hero_stand_down.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.init_image)
        self.up_image = pygame.image.load('images/hero_stand_up.png').convert_alpha()
        self.down_image = pygame.image.load('images/hero_stand_down.png').convert_alpha()
        self.left_image = pygame.image.load('images/hero_stand_left.png').convert_alpha()
        self.right_image = pygame.image.load('images/hero_stand_right.png').convert_alpha()
        self.up_move_image = []
        self.up_move_image.extend([
            pygame.image.load('images/hero_move_up1.png').convert_alpha(),\
            pygame.image.load('images/hero_move_up2.png').convert_alpha()
        ])
        self.down_move_image = []
        self.down_move_image.extend([
            pygame.image.load('images/hero_move_down1.png').convert_alpha(), \
            pygame.image.load('images/hero_move_down2.png').convert_alpha()
        ])

        self.left_move_image = []
        self.left_move_image.extend([
            pygame.image.load('images/hero_move_left1.png').convert_alpha(), \
            pygame.image.load('images/hero_move_left2.png').convert_alpha()
        ])

        self.right_move_image = []
        self.right_move_image.extend([
            pygame.image.load('images/hero_move_right1.png').convert_alpha(), \
            pygame.image.load('images/hero_move_right2.png').convert_alpha()
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
        if self.rect.bottom < self.world_height:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.world_height

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

    def level_up(self):
        self.level += 1
        self.health = 100 + (self.level - 1) * 50
        self.attack = 5 + (self.level - 1) * 2
        self.exp = 0

