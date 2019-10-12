import pygame
import random
import sys
import start_up
import main
import const


#importing pictures for game
start_bg = pygame.image.load('photos/start.png')
start_bg = pygame.transform.scale(start_bg,(const.WIDTH, const.HEIGHT-16))

bg_HELL = pygame.image.load('photos/hell.png')
bg_HELL = pygame.transform.scale(bg_HELL,(const.WIDTH + 100, const.HEIGHT))

bg_PURGATORY = pygame.image.load('photos/purg-1.jpeg')
bg_PURGATORY = pygame.transform.scale(bg_PURGATORY,(const.WIDTH, const.HEIGHT))

bg_HEAVEN = pygame.image.load('photos/h-1.png')
bg_HEAVEN = pygame.transform.scale(bg_HEAVEN,(const.WIDTH, const.HEIGHT))

#game image for objects
fire_ball = pygame.image.load('photos/fire_ball.png')
fire_ball = pygame.transform.scale(fire_ball,(const.enemy_size + 10, const.enemy_size + 10))

rock_ball = pygame.image.load('photos/round-rock.png')
rock_ball = pygame.transform.scale(rock_ball,(const.enemy_size + 15, const.enemy_size + 15))

orb = pygame.image.load('photos/orb.png')
orb = pygame.transform.scale(orb,(const.enemy_size + 15, const.enemy_size + 15))

dante = pygame.image.load('photos/dante.png')
dante = pygame.transform.scale(dante, (const.player_size - 10, const.player_size + 20))

