import start_up
import game_func
import game_images
import main
import random
import pygame
#constants

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)
PURPLE = (204, 204, 255)
BROWN = (97, 67, 69)
D_BROWN = (29,23,30)
D_GREEN = (0, 51, 51)

PURGATOYR_SCORE = 60
PARADISO_SCORE = 111

#intialising variables NOT ACTUALLY CONSTANTS
player_size = 60
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

SPEED = 10

game_over = False

score = 0