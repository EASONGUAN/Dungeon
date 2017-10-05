import pygame
import sys
import traceback
import hero
import soldier
import time
import Trees

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

white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0

def image_flash(object, time):
    pass


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def message(text):
    large_text = pygame.font.Font("freesansbold.ttf", 60)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((width / 2), (height / 2))
    screen.blit(text_surf, text_rect)
    pygame.display.update()

    time.sleep(2)

def game_over():
    message("Game Over")

movement = []

def main():
    count_kill = 0
    delay = 100
    my_hero = hero.Hero((45, 45), bg_size[0], bg_size[1])

    soldier_one = soldier.SoldierTypeOne((90, 90), bg_size[0], bg_size[1], 1)
    soldier_two = soldier.SoldierTypeOne((180, 180), bg_size[0], bg_size[1], 2)
    soldier_three = soldier.SoldierTypeOne((300, 300), bg_size[0], bg_size[1], 3)
    soldier_four = soldier.SoldierTypeTwo((90, 90), bg_size[0], bg_size[1], 4)
    soldier_five = soldier.SoldierTypeTwo((180, 180), bg_size[0], bg_size[1], 5)
    soldier_six = soldier.SoldierTypeTwo((300, 300), bg_size[0], bg_size[1], 6)
    soldier_group = pygame.sprite.Group()
    soldier_group.add(soldier_one)
    soldier_group.add(soldier_two)
    soldier_group.add(soldier_three)
    soldier_group.add(soldier_four)
    soldier_group.add(soldier_five)
    soldier_group.add(soldier_six)
    soldier_survive_group = pygame.sprite.Group()
    soldier_survive_group.add(soldier_one)
    soldier_survive_group.add(soldier_two)
    soldier_survive_group.add(soldier_three)
    soldier_survive_group.add(soldier_four)
    soldier_survive_group.add(soldier_five)
    soldier_survive_group.add(soldier_six)
    hero_group = pygame.sprite.Group()
    hero_group.add(my_hero)
    tree_one = Trees.TreeTypeOne(75, 125)
    root_one = Trees.RootTypeOne(75, 125)
    stabale = pygame.sprite.Group()
    stabale.add(tree_one)
    blocks = pygame.sprite.Group()
    blocks.add(root_one)

    playing = True
    movement = []
    while playing:
        fps = 60
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        key_pressed = pygame.key.get_pressed()
        can_move = True
        collide_root =  pygame.sprite.spritecollide(my_hero, blocks, False, pygame.sprite.collide_mask)
        if collide_root:
            can_move = False
        if can_move and key_pressed[K_UP] or key_pressed[K_w]:
            my_hero.moveup()
            movement.append("U")
        elif not can_move:
            my_hero.movedown()
            can_move = True
        if can_move and key_pressed[K_DOWN] or key_pressed[K_s]:
            my_hero.movedown()
            movement.append("D")
        elif not can_move:
            my_hero.moveup()
            can_move = True
        if can_move and key_pressed[K_LEFT] or key_pressed[K_a]:
            my_hero.moveleft()
            movement.append("L")
        elif not can_move:
            my_hero.moveright()
            can_move = True
        if can_move and key_pressed[K_RIGHT] or key_pressed[K_d]:
            my_hero.moveright()
            movement.append("R")
        elif not can_move:
            my_hero.moveleft()
            can_move = True
        screen.blit(background, (0, 0))
        if my_hero.active:
            screen.blit(my_hero.init_image, my_hero.rect)
            pygame.draw.line(screen, black, (my_hero.rect.left, my_hero.rect.top - 5),
                             (my_hero.rect.right, my_hero.rect.top - 5), 2)
            hero_health_remains = my_hero.health / 100
            if hero_health_remains > 0.5:
                energy_color = green
            else:
                energy_color = red
            pygame.draw.line(screen, energy_color, (my_hero.rect.left, my_hero.rect.top - 5),
                             (my_hero.rect.left + my_hero.rect.width * hero_health_remains, my_hero.rect.top - 5), 2)

        for sol in soldier_group:
            if sol.active:
                sol.move()
                screen.blit(sol.init_image, sol.rect)
                pygame.draw.line(screen, black, (sol.rect.left, sol.rect.top - 5),
                                 (sol.rect.right, sol.rect.top - 5), 2)
                sol_health_remains = sol.health/25
                if sol_health_remains > 0.5:
                    sol_color = green
                else:
                    sol_color = red
                pygame.draw.line(screen, sol_color, (sol.rect.left, sol.rect.top - 5),
                                 (sol.rect.left + sol.rect.width * sol_health_remains,
                                  sol.rect.top - 5), 2)
                hero_collide = pygame.sprite.spritecollide(sol, hero_group, False, pygame.sprite.collide_mask)
                if hero_collide:
                    if delay % 5 == 0:
                        my_hero.health -= sol.attack
                        sol.health -= my_hero.attack
                    if my_hero.health <= 0:
                        my_hero.active = False
                        playing = False
                    if sol.health <= 0:
                        sol.active = False
                    movement.append(sol.num)
        for stabale_object in stabale:
            screen.blit(stabale_object.init_image, stabale_object.rect)
        print(movement)
        movement = []

        delay -= 1
        if delay <= 0:
            delay = 100
        #print(my_hero.level, my_hero.health, my_hero.exp)
        clock.tick(fps)
        pygame.display.flip()
    screen.fill(WHITE)
    # game_over()
if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        print(movement)
        traceback.print_exc()
        pygame.quit()
        input()
