import start_up
import game_func
import game_images
import main
#startup

#speed
DIFF = 6
#amount of enemys
ENEMY_DIFF = 10
debug = False
#sets game difficulty
def option_set():
    #if __name__ == '__main__':
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
            option_set()
    
print("debug: " + str(debug))
print("speed: " + str(DIFF))
print("spawn_len: " + str(ENEMY_DIFF))