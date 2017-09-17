import pygame
import sys
import traceback
import hero
import world
import soldier

from pygame.locals import *
from random import *

bg_size = width, height = 480, 480
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Dungeon')

BLACK = 0, 0, 0
WHITE = 255, 255, 255

GAME_LEVEL = 1
NUM_WALLS = 10
NUM_ENEMIES = 0

pygame.init()
pygame.mixer.init()
background = pygame.image.load('images/background.png').convert()

soldier_startx = 100
soldier_starty = 100
soldier_speed = 4
soldier_width = 100
soldier_height = 100


def main():
    delay = 100
    my_hero = hero.Hero((45, 45), bg_size[0], bg_size[1])

    soldier_one = soldier.SoldierTypeOne((90, 90), bg_size[0], bg_size[1])
    soldier_two = soldier.SoldierTypeOne((180, 180), bg_size[0], bg_size[1])
    soldier_three = soldier.SoldierTypeOne((300, 300), bg_size[0], bg_size[1])

    soldier_list = [soldier_one, soldier_two, soldier_three]

    playing = True

    while playing:
        fps = 60
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP] or key_pressed[K_w]:
            my_hero.moveup()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            my_hero.movedown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            my_hero.moveleft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            my_hero.moveright()

        screen.blit(background, (0, 0))
        if my_hero.active:
            screen.blit(my_hero.init_image, my_hero.rect)

        for sol in soldier_list:
            screen.blit(sol.init_image, sol.rect)
            sol.move()


        clock.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
