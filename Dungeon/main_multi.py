import pygame
import sys
import traceback
import hero
import world
import soldier
import socket
import time
import pickle

from pygame.locals import *
from random import *

bg_size = width, height = 480, 480
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('Dungeon')

BLACK = 0, 0, 0
WHITE = 255, 255, 255

white = 255, 255, 255
black = 0, 0, 0
green = 0, 255, 0
red = 255, 0, 0

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


def text_objects(text, font):
    text_surface = font.render(text, True, BLACK)
    return text_surface, text_surface.get_rect()


def message(text):
    large_text = pygame.font.Font("freesansbold.ttf", 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((width / 2), (height / 2))
    screen.blit(text_surf, text_rect)
    pygame.display.update()

    time.sleep(2)


def wait_connect():
    message("Waiting")


def connect():

    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    # get local machine name
    host = socket.gethostname()

    port = 9999

    # connection to hostname on the port.
    sock.connect((host, port))

    # Receive no more than 1024 bytes

    return sock


def main():
    delay = 100
    my_hero = hero.Hero((45, 45), bg_size[0], bg_size[1])
    other_hero = hero.Hero((45, 45), bg_size[0], bg_size[1])

    soldier_one = soldier.SoldierTypeOne((90, 90), bg_size[0], bg_size[1], 1)
    soldier_two = soldier.SoldierTypeOne((180, 180), bg_size[0], bg_size[1], 2)
    soldier_three = soldier.SoldierTypeOne((300, 300), bg_size[0], bg_size[1], 3)

    soldier_group = pygame.sprite.Group()
    soldier_group.add(soldier_one)
    soldier_group.add(soldier_two)
    soldier_group.add(soldier_three)
    #soldier_list = [soldier_one, soldier_two, soldier_three]

    hero_group = pygame.sprite.Group()
    hero_group.add(my_hero)

    playing = True

    the_server = connect()

    while True:
        try:
            abc = the_server.recv(4096)
        except socket.error:
            screen.fill(WHITE)
            wait_connect()
            pygame.display.update()
            pass
        else:
            break

    print(abc.decode('ascii'))
    movement = []

    while playing:
        fps = 60
        clock = pygame.time.Clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        #Hero movement ==========================================

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP] or key_pressed[K_w]:
            my_hero.moveup()
            movement.append("U")
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            my_hero.movedown()
            movement.append("D")
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            my_hero.moveleft()
            movement.append("L")
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            my_hero.moveright()
            movement.append("R")
        else:
            movement.append("S")

        # Collision =============================================

        for sol in soldier_group:
            hero_collide = pygame.sprite.spritecollide(sol, hero_group, False, pygame.sprite.collide_mask)
            if hero_collide:
                if delay % 5 == 0:
                    my_hero.health -= sol.attack/10
                    sol.health -= my_hero.attack/10
                if my_hero.health <= 0:
                    my_hero.active = False
                    playing = False
                if sol.health <= 0:
                    sol.active = False
                movement.append(sol.num)
                movement.append("H")


        # This is to tell the other side to move their soldier
        movement.append("M")
        data = pickle.dumps(movement)
        the_server.send(data)

        print(movement)
        movement = []


        receive = the_server.recv(4096)
        other_move = pickle.loads(receive)

        for move in other_move:
            if move == "U":
                other_hero.moveup()
            if move == "R":
                other_hero.moveright()
            if move == "L":
                other_hero.moveleft()
            if move == "D":
                other_hero.movedown()
            if move == "M":
                for sol in soldier_group:
                    sol.move()

        for move in other_move:
            if isinstance(move, int):
                for sol in soldier_group:
                    if sol.num == move:
                        other_hero.health -= sol.attack / 10
                        sol.health -= my_hero.attack / 10
                    if other_hero.health <= 0:
                        other_hero.active = False
                        playing = False
                    if sol.health <= 0:
                        sol.active = False

        #Falsh screen here, do all the graphic stuff below =================================

        screen.blit(background, (0, 0))

        if my_hero.active:
            screen.blit(my_hero.init_image, my_hero.rect)
            screen.blit(other_hero.init_image, other_hero.rect)

            pygame.draw.line(screen, black, (my_hero.rect.left, my_hero.rect.top - 5),
                             (my_hero.rect.right, my_hero.rect.top - 5), 2)

            pygame.draw.line(screen, black, (other_hero.rect.left,other_hero.rect.top - 5),
                             (other_hero.rect.right, other_hero.rect.top - 5), 2)

            hero_health_remains = my_hero.health / 100
            other_hero_health_remains = other_hero.health / 100

            if hero_health_remains > 0.5:
                my_energy_color = green
            else:
                my_energy_color = red

            if  other_hero_health_remains > 0.5:
                other_energy_color = green
            else:
                other_energy_color = red

            pygame.draw.line(screen, my_energy_color, (my_hero.rect.left, my_hero.rect.top - 5),
                             (my_hero.rect.left + my_hero.rect.width * hero_health_remains, my_hero.rect.top - 5), 2)

            pygame.draw.line(screen, other_energy_color, (other_hero.rect.left, other_hero.rect.top - 5),
                             (other_hero.rect.left + other_hero.rect.width * other_hero_health_remains, other_hero.rect.top - 5), 2)

        for sol in soldier_group:
            if sol.active:
                screen.blit(sol.init_image, sol.rect)
                pygame.draw.line(screen, black, (sol.rect.left, sol.rect.top - 5),
                                     (sol.rect.right, sol.rect.top - 5), 2)
                sol_health_remains = sol.health / 25

                if sol_health_remains > 0.5:
                    sol_color = green
                else:
                    sol_color = red

                pygame.draw.line(screen, sol_color, (sol.rect.left, sol.rect.top - 5),
                                     (sol.rect.left + sol.rect.width * sol_health_remains,
                                      sol.rect.top - 5), 2)

                screen.blit(sol.init_image, sol.rect)


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
