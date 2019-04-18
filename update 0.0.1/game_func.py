import pygame
import random
import sys
import time
import os
import start_up
import const
import game_images
import main


#intialize screen
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT + 3))
#intialize font
myFont = pygame.font.SysFont("monospace", 35)
#intializing the 'clock' for fps
clock = pygame.time.Clock()

#functions all put below
#function for increasing the speed
def set_speed(score, SPEED):
    SPEED = (score / start_up.DIFF + 9) 
    return SPEED

#creates enemy object and randomly places 
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < start_up.ENEMY_DIFF and delay < 0.1:
        x_pos = random.randint(0,const.WIDTH-const.enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

#draws the enemy
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        #draws collisons squares
        #pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], const.enemy_size, const.enemy_size))
        #draws image over square
        screen.blit(enemy_image(const.score),(const.enemy_pos[0] - 5,const.enemy_pos[1] - 5))

#updates the position of the enemy (physics engine lol)
def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < const.HEIGHT:
            enemy_pos[1] += const.SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score

#checks if there is a colision
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

#caculates if enemy or player are in side eachothers colision boxing and retruns t/f
def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + const.player_size)) or (p_x >= e_x and p_x < (e_x+const.enemy_size)):
        if (e_y >= p_y and e_y < (p_y + const.player_size)) or (p_y >= e_y and p_y < (e_y+const.enemy_size)):
            return True
    return False

#calculates what picture to be put on to the enemy based on where the player is
def enemy_image(s):
    if s > const.PURGATOYR_SCORE and s <= const.PARADISO_SCORE:
        return game_images.rock_ball
    elif s > const.PARADISO_SCORE:
        return game_images.orb
    else:
        return game_images.fire_ball

#checks which level the player is on and returns the background image of the level
def level_checker(s):
    if s > const.PURGATOYR_SCORE and s <= const.PARADISO_SCORE:
        return game_images.bg_PURGATORY
    elif s > const.PARADISO_SCORE:
        return game_images.bg_HEAVEN
    else:
        return game_images.bg_HELL

#checks which level the player is on and returns the name of the level
def text_stage(s):
    if s < const.PURGATOYR_SCORE:
        return 'INFERNO'
    elif s > const.PURGATOYR_SCORE and s <= const.PARADISO_SCORE:
        return 'PURGATORIO'
    elif s > const.PARADISO_SCORE:
        return 'PARADISO'
    else:
        return 'abandon all hope ye who enter here'

#function for pausing the game
def pause_checker():
    screen.fill(const.PURPLE)
    screen.blit(level_checker(const.score),(0,0))
    text = 'PAUSED'
    label = myFont.render(text, 1, (102, 102, 255))
    screen.blit(label, (const.WIDTH/2 - 50, const.HEIGHT - 500))
    
    pygame.display.update()

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    sys.exit()

#called once player dies, and displays score [CSV HIGHSCORE sheet in the works]
def end_screen():
    #file_name = 'high_score.csv'
    #file = []
    #if os.path.isfile(file_name):
        #   print("***file already created***")
        #  with open(file_name, 'a') as f_csv:
        #     next(f_csv)
        #    for line in f_csv:
            #       print(line)
            #      file.append(line)
            #     pass
    screen.fill(const.BACKGROUND_COLOR)
    screen.blit(level_checker(const.score),(0,0))
    #dante image
    screen.blit(game_images.dante,(const.player_pos[0] + 7,const.player_pos[1] - 10))
    #text for end screen
    text = 'GAME_OVER'
    score_txt = "Score: " + str(const.score)
    label = myFont.render(text, 1, const.RED) #(102, 102, 255)
    score_label = myFont.render(score_txt, 1, const.YELLOW)
    screen.blit(label, (const.WIDTH/2 - ((len(text)) * 9), const.HEIGHT - 500))
    screen.blit(score_label, (const.WIDTH/2 - ((len(text)) * 5.5), const.HEIGHT - 450))
    
    pygame.display.update()

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_SPACE:
                    print(" \n ***re-running*** \n")
                    #call rerun script maybe main
                elif event.key == pygame.K_q:
                    sys.exit()

#the start screen of the game 
def start_screen():
    #background
    screen.fill(const.D_BROWN) #dark brown
    screen.blit(game_images.start_bg,(0,0))
    #loading font and text for start screen
    myfont = pygame.font.SysFont('pressstart2pttf', 20)
    textsurface = myfont.render('abandon all hope ye who enter here', False, const.BROWN)  
    screen.blit(textsurface,(57, const.HEIGHT - 17))

    title = pygame.font.SysFont('pressstart2pttf', 38)
    titleSurface = title.render('Dante\'s Adventure', False, const.D_GREEN)
    screen.blit(titleSurface,(80, 48))

    screen.blit(game_images.dante,(const.player_pos[0] + 7,const.player_pos[1] - 10))
    
    pygame.display.update()

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    sys.exit()


def main_run():
    #main game loop
    while not const.game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                x = const.player_pos[0]
                y = const.player_pos[1]
                #main key functionality for in game
                if event.key == pygame.K_LEFT:
                    if start_up.debug == False:
                        if const.player_pos[0] > 35:
                            x -= const.player_size
                        else:
                            print("At left wall")
                    else:
                        x -= const.player_size
                elif event.key == pygame.K_RIGHT:
                    if start_up.debug == False:
                        if const.player_pos[0] < const.WIDTH - 80:
                            x += const.player_size
                        else:
                            print("at right wall ")
                    else:
                        x += const.player_size
                elif event.key == pygame.K_p:
                    pause_checker()
                player_pos = [x,y]

        #draws background color(black)
        screen.fill(const.BACKGROUND_COLOR)
        #draws background image
        screen.blit(level_checker(const.score),(0,0))
        #displays text onto screen 1)sets font, 2)sets text, anti-alias, and color, 3)puts text on screen
        myfont = pygame.font.SysFont('pressstart2pttf', 20)
        textsurface_main = myfont.render(text_stage(const.score), False, const.BACKGROUND_COLOR)
        screen.blit(textsurface_main,(const.WIDTH / 2 - (len(text_stage(const.score)) * 12) , const.HEIGHT - 17)) #puts text and position on screen(WIDTH,HEIGHT)

        #creates enemy object
        drop_enemies(const.enemy_list)
        #calculates score
        score = update_enemy_positions(const.enemy_list, score)
        #calculates speed
        SPEED = set_speed(score, SPEED)

        #prints score onto main game screen
        text = "Score:" + str(score)
        label = myFont.render(text, 1, const.YELLOW)
        screen.blit(label, (const.WIDTH-200, const.HEIGHT-40)) #position of text

        if collision_check(const.enemy_list, player_pos):
            game_over = True
            break
        #draws the enemy on the screen
        draw_enemies(const.enemy_list)
        #draws players colision box
        #play = pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

        #puts players image on screen over c-box
        screen.blit(game_images.dante,(player_pos[0] + 7,player_pos[1] - 10))
        clock.tick(30)
        #updates the screen 
        pygame.display.update()