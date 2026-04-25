import pygame
from pygame.locals import *
import sys
import random
import csv
import time

pygame.font.init()
pygame.init()

large_font = pygame.font.SysFont('Comic Sans MS', 38)
medium_font = pygame.font.SysFont('Comic Sans MS', 28)
small_font = pygame.font.SysFont('Comic Sans MS', 16)

window = pygame.display.set_mode((600,704))

# constants
figures = [
        [[["0","2","0"],["2","2","2"]],
        [["0","2","0"],["0","2","2"],["0","2","0"]],
        [["2","2","2"],["0","2","0"]],
        [["0","2","0"],["2","2","0"],["0","2","0"]]], # _|_ looking one

        [[["2","2","2","2"]],
        [["2"],["2"],["2"],["2"]]], # | looking one

        [[["2","2"],["2","2"]]], # cube

        [[["2","0","0","0"],["2","2","2","2"]],
        [["2","2"],["2","0"],["2","0"],["2","0"]],
        [["2","2","2","2"],["0","0","0","2"]],
        [["0","2"],["0","2"],["0","2"],["2","2"]]], # |___ looking one

        [[["0","0","0","2"],["2","2","2","2"]],
        [["2","0"],["2","0"],["2","0"],["2","2"]],
        [["2","2","2","2"],["2","0","0","0"]],
        [["2","2"],["0","2"],["0","2"],["0","2"]]], # ___| looking one

        [[["0","2","2"],["2","2","0"]],
        [["2","0"],["2","2"],["0","2"]]], # _|- looking one

        [[["2","2","0"],["0","2","2"]],
        [["0","2"],["2","2"],["2","0"]]] # Z looking one
        ]

# variables
completed_row = ["1","3","3","3","3","3","3","3","3","3","3","1"]
score = 0
turn = 0


# ALL FUNCTIONS
def Row_Complete():
    global score
    row_complete = False
    # checking if any rows are complete
    for row_i in range(len(modified_tetris)):
        if modified_tetris[row_i] == completed_row:
            modified_tetris[row_i] = ["1","0","0","0","0","0","0","0","0","0","0","1"]
            row_completed = row_i
            row_complete = True
            score += 100
            break
    # moving all the rows on top of it down
    if row_complete:
        for row_i in range(len(modified_tetris)-2,-1,-1):
            if row_i < row_completed:
                modified_tetris[row_i+1] = modified_tetris[row_i]
                modified_tetris[row_i] = ["1","0","0","0","0","0","0","0","0","0","0","1"]

def Rotate_Piece():
    # if none of the indexes intercept - rotate the figure
    if random_figure == 0:
        for i in range(len(figures[0][turn])):
            for k in range(len(figures[0][turn][i])):
                if figures[0][turn][i][k] == "2":
                    if turn == 2:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k+1] = "2"
                    else:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k] = "2"
    elif random_figure == 1:
        for i in range(len(figures[1][turn])):
            for k in range(len(figures[1][turn][i])):
                if figures[1][turn][i][k] == "2":
                    if turn == 1:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k+3] = "2"
                    else:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k-1] = "2"
    elif random_figure == 3:
        for i in range(len(figures[3][turn])):
            for k in range(len(figures[3][turn][i])):
                if figures[3][turn][i][k] == "2":
                    if turn in [0,2]:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k+1] = "2"
                    elif turn == 3:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k-1] = "2"
                    else:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k] = "2"
    elif random_figure == 4:
        for i in range(len(figures[4][turn])):
            for k in range(len(figures[4][turn][i])):
                if figures[4][turn][i][k] == "2":
                    if turn in [0,2]:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k+1] = "2"
                    elif turn == 3:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k-1] = "2"
                    else:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k] = "2"
    elif random_figure == 5:
        for i in range(len(figures[5][turn])):
            for k in range(len(figures[5][turn][i])):
                if figures[5][turn][i][k] == "2":
                    if turn == 0:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k+1] = "2"
                    else:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k] = "2"
    elif random_figure == 6:
        for i in range(len(figures[6][turn])):
            for k in range(len(figures[6][turn][i])):
                if figures[6][turn][i][k] == "2":
                    if turn == 0:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k+1] = "2"
                    else:
                        modified_tetris[figure_start_i[0]+i][figure_start_i[1]+k] = "2"

def Saving_Rotation_Indexes():
    # SAVING ALL INDEXES THAT WILL BE USED UP BY A FIGURE AFTER ITS BEEN ROTATED
    if random_figure == 0:
        for i in range(len(figures[0][turn])):
            for k in range(len(figures[0][turn][i])):
                if figures[0][turn][i][k] == "2":
                    if turn == 2:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k+1])
                    else:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k])
    elif random_figure == 1:
        for i in range(len(figures[1][turn])):
            for k in range(len(figures[1][turn][i])):
                if figures[1][turn][i][k] == "2":
                    if turn == 1:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k+3])
                    else:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k-1])
    elif random_figure == 3:
        for i in range(len(figures[3][turn])):
            for k in range(len(figures[3][turn][i])):
                if figures[3][turn][i][k] == "2":
                    if turn in [0,2]:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k+1])
                    elif turn == 3:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k-1])
                    else:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k])
    elif random_figure == 4:
        for i in range(len(figures[4][turn])):
            for k in range(len(figures[4][turn][i])):
                if figures[4][turn][i][k] == "2":
                    if turn in [0,2]:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k+1])
                    elif turn == 3:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k-1])
                    else:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k])
    elif random_figure == 5:
        for i in range(len(figures[5][turn])):
            for k in range(len(figures[5][turn][i])):
                if figures[5][turn][i][k] == "2":
                    if turn == 0:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k+1])
                    else:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k])
    elif random_figure == 6:
        for i in range(len(figures[6][turn])):
            for k in range(len(figures[6][turn][i])):
                if figures[6][turn][i][k] == "2":
                    if turn == 0:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k+1])
                    else:
                        new_coordinates.append([figure_start_i[0]+i,figure_start_i[1]+k])


# drawing the map
modified_tetris = []
with open("tetris.csv", newline="") as file:
    everything = csv.reader(file)
    everything = list(everything)
row_ = []
for row_i,row in enumerate(everything):
    for pixel_i,pixel in enumerate(row):
        if pixel == "1":
            pygame.draw.rect(window, "grey", (pixel_i*32,row_i*32, 32,32))
        row_.append(pixel)
    modified_tetris.append(row_)
    row_ = []
        

# adding the first piece at the very start of the game
random_figure = random.randint(0,len(figures)-1)
for i,row in enumerate(figures[random_figure][0]):
    for k,column in enumerate(row):
        if column == "2":
            modified_tetris[i][6-len(row)//2+k] = "2"
next_piece = random.randint(0,len(figures)-1)

last_time = pygame.time.get_ticks()
falling = True
while True:
    window.fill("black")

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # LEFT MOVEMENT
            if event.key == pygame.K_LEFT:
                coordinates_to_be_moved = []
                can_be_moved = True

                # CHECKING FOR COLLISIONS
                for row_i in range(len(modified_tetris)):
                    for pixel_i in range(len(row)):
                        if modified_tetris[row_i][pixel_i] == "2":
                            coordinates_to_be_moved.append([row_i,pixel_i-1])
                for y,x in coordinates_to_be_moved:
                    if modified_tetris[y][x] in "13":
                        can_be_moved = False
                        break
                if not can_be_moved:
                    break

                for row_i in range(len(modified_tetris)):
                    for pixel_i in range(len(row)):
                        if modified_tetris[row_i][pixel_i] == "2":
                            modified_tetris[row_i][pixel_i-1] = "2"
                            modified_tetris[row_i][pixel_i] = "0"
            # RIGHT MOVEMENT
            if event.key == pygame.K_RIGHT:
                coordinates_to_be_moved = []
                can_be_moved = True

                # CHECKING FOR COLLISIONS
                for row_i in range(len(modified_tetris)):
                    for pixel_i in range(len(row)):
                        if modified_tetris[row_i][pixel_i] == "2":
                            coordinates_to_be_moved.append([row_i,pixel_i+1])
                for y,x in coordinates_to_be_moved:
                    if modified_tetris[y][x] in "13":
                        can_be_moved = False
                        break
                if not can_be_moved:
                    break

                for row_i in range(len(modified_tetris)):
                    for pixel_i in range(len(row)):
                        if modified_tetris[row_i][10-pixel_i] == "2":
                            modified_tetris[row_i][10-pixel_i+1] = "2"
                            modified_tetris[row_i][10-pixel_i] = "0"

            # ROTATION
            if event.key == pygame.K_UP:
                start_found = False
                new_coordinates = []
                figure_indexes = []
                can_rotate = True

                # FINDING BOUNDARIES OF A PIECE FALLING DOWN
                if random_figure != 2:
                    for row_i in range(len(modified_tetris)):
                        for pixel_i in range(len(row)):
                            if modified_tetris[row_i][pixel_i] == "2":
                                if not start_found:
                                    figure_start_i = (row_i,pixel_i-1)
                                    start_found = True
                                figure_indexes.append([row_i,pixel_i])
                                modified_tetris[row_i][pixel_i] = "0" # deleting a piece so that it can be re-drawn after a rotation

                turn += 1
                if turn == len(figures[random_figure]):
                    turn = 0

                Saving_Rotation_Indexes()


                # CHECKING WHETHER THE FIGURE COLLIDES WITH ANYTHING WHEN BEING ROTATED
                for y,x in new_coordinates:
                    if modified_tetris[y][x] in "13":
                        can_rotate = False
                        break
                # if indexes to intercept - don't rotate the figure but re-draw it on the screen
                if not can_rotate:
                    for y,x in figure_indexes:
                        modified_tetris[y][x] = "2"
                    turn -= 1
                    break
                
                Rotate_Piece()
            
            # MOVEMENT DOWN
            if event.key == pygame.K_DOWN:
                # CHECKING FOR COLLISIONS
                figure_indexes = []
                for row_i in range(len(modified_tetris)-2,-1,-1):
                    for pixel in range(len(modified_tetris[row_i])):
                        if modified_tetris[row_i][pixel] == "2": # checking how long the figure is(its boundaries)
                            figure_indexes.append(pixel)
                    for index in figure_indexes: # if any of those indexes collide with the row underneeth - stop moving
                        if modified_tetris[row_i+1][index] in "13":
                            falling = False
                            break
                for row_i in range(len(modified_tetris)-2,-1,-1): # ITERATING THROUGH EACH ROW TO SEE WHETHER ANY PART OF A FIGURE FALLING DOWN COLLIDE WITH FIGURES UNDERNEETH
                    if falling: # if not collisions, then proceed to move the figure down
                        for pixel_i in range(len(row)):
                            if modified_tetris[row_i][pixel_i] == "2": # if is part of the figure then..
                                if modified_tetris[row_i+1][pixel_i] not in "13":
                                    modified_tetris[row_i+1][pixel_i] = "2" # move down
                                    modified_tetris[row_i][pixel_i] = "0"
                                    falling = True
                                else:
                                    falling = False
                                    break
                    if not falling:
                        break


    
    current_time = pygame.time.get_ticks()
    if current_time - last_time >= 300: # making pieces fall every 0.3 seconds
        last_time = current_time
        figure_indexes = []
        for row_i in range(len(modified_tetris)-2,-1,-1):
            for pixel in range(len(modified_tetris[row_i])):
                if modified_tetris[row_i][pixel] == "2": # checking how long the figure is(its boundaries)
                    figure_indexes.append(pixel)
            for index in figure_indexes: # if any of those indexes collide with the row underneeth - stop moving
                if modified_tetris[row_i+1][index] in "13":
                    falling = False
                    break
        for row_i in range(len(modified_tetris)-2,-1,-1): # ITERATING THROUGH EACH ROW TO SEE WHETHER ANY PART OF A FIGURE FALLING DOWN COLLIDE WITH FIGURES UNDERNEETH
            if falling: # if not collisions, then proceed to move the figure down
                for pixel_i in range(len(row)):
                    if modified_tetris[row_i][pixel_i] == "2": # if is part of the figure then..
                        if modified_tetris[row_i+1][pixel_i] not in "13":
                            modified_tetris[row_i+1][pixel_i] = "2" # move down
                            modified_tetris[row_i][pixel_i] = "0"
                            falling = True
                        else:
                            falling = False
                            break
            if not falling:
                break


    # checking if any rows are complete
    Row_Complete()


    if not falling: # IF THE FIGURE STOPPED FALLING - SPAWN A NEW ONE AND MARK THE PREVIOUS ONE AS *finished*
        if modified_tetris[0] != ["1","0","0","0","0","0","0","0","0","0","0","1"]:
            you_lost_text = large_font.render('You lost', False, (255, 255, 255))
            window.blit(you_lost_text, (window.get_width()//2-100, window.get_height()//2-44))
            score_text = medium_font.render(f'Your score is {score}', False, (255, 255, 255))
            window.blit(score_text, (window.get_width()//2-84,window.get_height()//2-100))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
            sys.exit()


        # changing all 2s to 3s to understand that they have been placed
        for row_i in range(len(modified_tetris)):
            for pixel_i in range(len(row)):
                if modified_tetris[row_i][pixel_i] == "2":
                    modified_tetris[row_i][pixel_i] = "3"

        random_figure = next_piece
        for i,row in enumerate(figures[random_figure][0]):
            for k,column in enumerate(row):
                if column == "2":
                    modified_tetris[i][6-len(row)//2+k] = "2"

        next_piece = random.randint(0,len(figures)-1) # generating the next piece

        turn = 0
        falling = True


    # DRAWING THE MAP + EXISTENT FIGURES
    for row_i,row in enumerate(modified_tetris):
        for pixel_i,pixel in enumerate(row):
            if pixel == "1":
                pygame.draw.rect(window, "grey", (pixel_i*32,row_i*32, 32,32))
            elif pixel == "2":
                pygame.draw.rect(window, "red", (pixel_i*32,row_i*32, 32,32))
            elif pixel == "3":
                pygame.draw.rect(window, "green", (pixel_i*32,row_i*32, 32,32))
    
    # USER SCORE + NEXT PIECE TO BE SPAWNED
    score_text = small_font.render(f'Your score is {score}', False, (255, 255, 255))
    window.blit(score_text, (window.get_width()-(window.get_width()-12*32)//2-84,window.get_height()//12))
    next_piece_text = small_font.render('Next piece is:', False, (255, 255, 255))
    window.blit(next_piece_text, (window.get_width()-(window.get_width()-12*32)//2-64,window.get_height()//6))
    for i_,i__ in enumerate(figures[next_piece][0]):
        for k_,k__ in enumerate(i__):
            if k__ == "2":
                pygame.draw.rect(window, "blue", (32*k_+window.get_width()-(window.get_width()-12*32)//2-40,32*i_+window.get_height()//4, 32,32))



    pygame.display.update()
    pygame.time.Clock().tick(60)