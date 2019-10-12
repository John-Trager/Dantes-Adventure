import pygame
import random
import sys
import time
import os

#speed
DIFF = 6
#amount of enemys
ENEMY_DIFF = 10
debug = False
#sets game difficulty

if __name__ == '__main__':
    print(__name__)
    user = input(" \n Hard, Medium or Easy: ").upper()

    if user == "H":
        DIFF = 5
        ENEMY_DIFF = 13
    elif user == "M":
        DIFF = 6
        ENEMY_DIFF = 10
    elif user == "E":
        DIFF = 8
        ENEMY_DIFF = 7
    elif user == 'C':
        debug = True
        DIFF = 5
        ENEMY_DIFF = 10
    else:
        print("Error selection not found \n running defualt")
        #option_set()


#runs game
def run():
    print("debug: " + str(debug))
    print("speed: " + str(DIFF))
    print("spawn_len: " + str(ENEMY_DIFF))

    pygame.init()
    pygame.display.set_caption("Dante")
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

    player_size = 60
    player_pos = [WIDTH/2, HEIGHT-2*player_size]

    enemy_size = 50
    enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
    enemy_list = [enemy_pos]

    SPEED = 10

    screen = pygame.display.set_mode((WIDTH, HEIGHT + 3))

    game_over = False

    score = 0
    #intializing the 'clock' for fps
    clock = pygame.time.Clock()
    #setting font
    myFont = pygame.font.SysFont("monospace", 35)

    #importing pictures for game
    start_bg = pygame.image.load('photos/start.png')
    start_bg = pygame.transform.scale(start_bg,(WIDTH, HEIGHT-16))

    bg_HELL = pygame.image.load('photos/hell.png')
    bg_HELL = pygame.transform.scale(bg_HELL,(WIDTH + 100, HEIGHT))

    bg_PURGATORY = pygame.image.load('photos/purg-1.jpeg')
    bg_PURGATORY = pygame.transform.scale(bg_PURGATORY,(WIDTH, HEIGHT))

    bg_HEAVEN = pygame.image.load('photos/h-1.png')
    bg_HEAVEN = pygame.transform.scale(bg_HEAVEN,(WIDTH, HEIGHT))
    
    #backup image
    #bg_DEFUALT = pygame.image.load('photos/background.png')
    #bg_DEFUALT = pygame.transform.scale(bg_DEFUALT,(WIDTH, HEIGHT))

    #game image for objects
    fire_ball = pygame.image.load('photos/fire_ball.png')
    fire_ball = pygame.transform.scale(fire_ball,(enemy_size + 10, enemy_size + 10))

    rock_ball = pygame.image.load('photos/round-rock.png')
    rock_ball = pygame.transform.scale(rock_ball,(enemy_size + 15, enemy_size + 15))

    orb = pygame.image.load('photos/orb.png')
    orb = pygame.transform.scale(orb,(enemy_size + 15, enemy_size + 15))

    dante = pygame.image.load('photos/dante.png')
    dante = pygame.transform.scale(dante, (player_size - 10, player_size + 20))
    
    #functions all put below
    #function for increasing the speed
    def set_speed(score, SPEED):
        SPEED = (score / DIFF + 9) 
        return SPEED

    #creates enemy object and randomly places 
    def drop_enemies(enemy_list):
        delay = random.random()
        if len(enemy_list) < ENEMY_DIFF and delay < 0.1:
            x_pos = random.randint(0,WIDTH-enemy_size)
            y_pos = 0
            enemy_list.append([x_pos, y_pos])
    
    #draws the enemy
    def draw_enemies(enemy_list):
        for enemy_pos in enemy_list:
            #draws collisons squares
            if debug == True:
                pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
            #draws image over square
            screen.blit(enemy_image(score),(enemy_pos[0] - 5,enemy_pos[1] - 5))

    #updates the position of the enemy (physics engine lol)
    def update_enemy_positions(enemy_list, score):
        for idx, enemy_pos in enumerate(enemy_list):
            if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
                enemy_pos[1] += SPEED
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

        if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
            if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
                return True
        return False

    #calculates what picture to be put on to the enemy based on where the player is
    def enemy_image(s):
        if s > PURGATOYR_SCORE and s <= PARADISO_SCORE:
            return rock_ball
        elif s > PARADISO_SCORE:
            return orb
        else:
            return fire_ball

    #checks which level the player is on and returns the background image of the level
    def level_checker(s):
        if s > PURGATOYR_SCORE and s <= PARADISO_SCORE:
            return bg_PURGATORY
        elif s > PARADISO_SCORE:
            return bg_HEAVEN
        else:
            return bg_HELL

    #checks which level the player is on and returns the name of the level
    def text_stage(s):
        if s < PURGATOYR_SCORE:
            return 'INFERNO'
        elif s > PURGATOYR_SCORE and s <= PARADISO_SCORE:
            return 'PURGATORIO'
        elif s > PARADISO_SCORE:
            return 'PARADISO'
        else:
            return 'abandon all hope ye who enter here'

    #function for pausing the game
    def pause_checker():
        screen.fill(PURPLE)
        screen.blit(level_checker(score),(0,0))
        text = 'PAUSED'
        label = myFont.render(text, 1, (102, 102, 255))
        screen.blit(label, (WIDTH/2 - 50, HEIGHT - 500))
        
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
        screen.fill(BACKGROUND_COLOR)
        screen.blit(level_checker(score),(0,0))
        screen.blit(dante,(player_pos[0] + 7,player_pos[1] - 10))
        #text for end screen
        text = 'GAME_OVER'
        score_txt = "Score: " + str(score)
        label = myFont.render(text, 1, RED) #(102, 102, 255)
        score_label = myFont.render(score_txt, 1, YELLOW)
        screen.blit(label, (WIDTH/2 - ((len(text)) * 9), HEIGHT - 500))
        screen.blit(score_label, (WIDTH/2 - ((len(text)) * 5.5), HEIGHT - 450))
        
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
                        run()
                    elif event.key == pygame.K_q:
                        sys.exit()

    #the start screen of the game 
    def start_screen():
        #background
        screen.fill(D_BROWN) #dark brown
        screen.blit(start_bg,(0,0))
        #loading font and text for start screen
        myfont = pygame.font.SysFont('pressstart2pttf', 20)
        textsurface = myfont.render('abandon all hope ye who enter here', False, BROWN)  
        screen.blit(textsurface,(57, HEIGHT - 17))

        title = pygame.font.SysFont('pressstart2pttf', 38)
        titleSurface = title.render('Dante\'s Adventure', False, D_GREEN)
        screen.blit(titleSurface,(80, 48))
    
        screen.blit(dante,(player_pos[0] + 7,player_pos[1] - 10))
        
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

    start_screen()

    #main game loop
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:

                x = player_pos[0]
                y = player_pos[1]
                #main key functionality for in game
                if event.key == pygame.K_LEFT:
                    if debug == False:
                        if player_pos[0] > 35:
                            x -= player_size
                        else:
                            print("At left wall")
                    else:
                        x -= player_size
                elif event.key == pygame.K_RIGHT:
                    if debug == False:
                        if player_pos[0] < WIDTH - 80:
                            x += player_size
                        else:
                            print("at right wall ")
                    else:
                        x += player_size
                elif event.key == pygame.K_p:
                    pause_checker()
                player_pos = [x,y]

        #draws background color(black)
        screen.fill(BACKGROUND_COLOR)
        #draws background image
        screen.blit(level_checker(score),(0,0))
        #displays text onto screen 1)sets font, 2)sets text, anti-alias, and color, 3)puts text on screen
        myfont = pygame.font.SysFont('pressstart2pttf', 20)
        textsurface_main = myfont.render(text_stage(score), False, BACKGROUND_COLOR)
        screen.blit(textsurface_main,(WIDTH / 2 - (len(text_stage(score)) * 12) , HEIGHT - 17)) #puts text and position on screen(WIDTH,HEIGHT)

        #creates enemy object
        drop_enemies(enemy_list)
        #calculates score
        score = update_enemy_positions(enemy_list, score)
        #calculates speed
        SPEED = set_speed(score, SPEED)

        #prints score onto main game screen
        text = "Score:" + str(score)
        label = myFont.render(text, 1, YELLOW)
        screen.blit(label, (WIDTH-200, HEIGHT-40)) #position of text

        if collision_check(enemy_list, player_pos):
            game_over = True
            break
        #draws the enemy on the screen
        draw_enemies(enemy_list)
        #draws players colision box
        if debug == True:
            play = pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

        #puts players image on screen over c-box
        screen.blit(dante,(player_pos[0] + 7,player_pos[1] - 10))
        clock.tick(30)
        #updates the screen 
        pygame.display.update()

    #call end game once player dies
    end_screen()

#runs whole program
run()
