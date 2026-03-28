import pygame
from pygame.locals import *
import random
import sys

pygame.init()
old_window = pygame.display.set_mode((1160, 776))

all_entities = []

# SPAWNING EVERYTHING
player = pygame.draw.rect(old_window, "blue", (old_window.get_width()//2,old_window.get_height()//2, 24,24))

walls = []
# WALLS GENERATION FUNCTIONS/PROCEDURES
def spawn_wall():
    walls.append(pygame.draw.rect(old_window, "red", (random.randint(0,old_window.get_width()),random.randint(0,old_window.get_height()), random.randint(6,200),random.randint(6,200))))
    for wall in range(len(walls)-1):
        while walls[-1].colliderect(walls[wall]) or walls[-1].colliderect(player):
            walls.pop(-1)
            walls.append(pygame.draw.rect(old_window, "red", (random.randint(0,old_window.get_width()),random.randint(0,old_window.get_height()), random.randint(6,200),random.randint(6,200))))
    all_entities.append(walls[-1])
for i in range(23):
    spawn_wall()
window = pygame.display.set_mode((960, 576))


# PLAYER PROCEDURES/FUNCTIONS
def player_collide():
    old_pos = player_move()
    for wall in walls:
        if player.colliderect(wall):
            for entity in all_entities:
                if abs(player.x - window.get_width()//2-150) <= 180:
                    entity.x -= old_pos[0] - player.x
                if abs(player.y - window.get_height()//2-150) <= 180:
                    entity.y -= old_pos[1] - player.y
            
            player.x = old_pos[0]
            player.y = old_pos[1]
    for chipmunk in chipmunks:
        if player.colliderect(chipmunk):
            chipmunks.remove(chipmunk)
def player_move():
    global player_speed
    diagon_mov = False

    cur_pos = (player.x,player.y)

    for i in range(2):
        for k in range(2):
            if player_dir_x[i] - player_dir_y[k] == 0 and player_dir_x[i] != 0 and player_dir_y[k] != 0:
                diagon_mov = True
                player_speed = 2
                break
            
        if player_dir_x[0] - player_dir_x[1] == -1:
            if window.get_width() - player.x >= 28:
                player.x += player_speed
        elif player_dir_x[0] - player_dir_x[1] == 1:
            if 0 - player.x <= -2:
                player.x -= player_speed
        
        if player_dir_y[0] - player_dir_y[1] == -1:
            if 0 - player.y <= -2:
                player.y -= player_speed
        elif player_dir_y[0] - player_dir_y[1] == 1:
            if window.get_height() - player.y >= 28:
                player.y += player_speed
        if not diagon_mov:
            player_speed = 3

    # CAMERA FOLLOWING THE PLAYER
    for entity in all_entities:
            if abs(player.x - window.get_width()//2-150) <= 180:
                entity.x += cur_pos[0] - player.x
            if abs(player.y - window.get_height()//2-150) <= 180:
                entity.y += cur_pos[1] - player.y
        
    return cur_pos

# CHIPMUNKS PROCEDURES/FUNCTIONS
chipmunks = []
chipmunk_speed = 2
def create_chipmunk():
    while True:
        collide = False
        size = random.randint(4,20)
        new_chipmunk = pygame.draw.rect(old_window, "green", (random.randint(0,old_window.get_width()-size),random.randint(0,old_window.get_height()-size-1), size,size))
        if new_chipmunk.colliderect(player):
            collide = True
            continue
        for wall in walls:
            if new_chipmunk.colliderect(wall):
                collide = True
                break
        if not collide:
            chipmunks.append(new_chipmunk)
            all_entities.append(new_chipmunk)
            break

        
directions = []
def chipmunk_rand_move():
    ran_dir_x = random.randint(0,1)
    ran_dir_y = random.randint(0,1)
    if ran_dir_x == 0:
        dir_x = -1
    else:
        dir_x = 1
    if ran_dir_y == 0:
        dir_y = 1
    else:
        dir_y = -1
    directions.append([dir_x,dir_y])

def chipmunk_move(chipmunk, dir_x,dir_y):
    if dir_x == 1:
        chipmunk.x += chipmunk_speed
    else:
        chipmunk.x -= chipmunk_speed
    if dir_y == 1:
        chipmunk.y += chipmunk_speed
    else:
        chipmunk.y -= chipmunk_speed
def chipmunks_collide(chipmunk, index, dir_x, dir_y):
    for wall in walls:
        if chipmunk.colliderect(wall):
            if chipmunk.right >= wall.left and chipmunk.left <= wall.left:
                directions[index][0] = -dir_x
            if chipmunk.left <= wall.right and chipmunk.right >= wall.right:
                directions[index][0] = -dir_x
            if chipmunk.bottom >= wall.top and chipmunk.top <= wall.top:
                directions[index][1] = -dir_y
            if chipmunk.top <= wall.bottom and chipmunk.bottom >= wall.bottom:
                directions[index][1] = -dir_y
    if chipmunk.left <= 0 or chipmunk.right >= window.get_width():
        directions[index][0] = -dir_x
    if chipmunk.top <= 0 or chipmunk.bottom >= window.get_height():
        directions[index][1] = -dir_y
    chipmunk_move(chipmunk, directions[index][0],directions[index][1])
            
for _ in range(12):
    create_chipmunk()
    chipmunk_rand_move()

# PLAYER DETAILS
player_speed = 1
player_dir_x = [0,0]
player_dir_y = [0,0]

last_time = pygame.time.get_ticks()
while True:
    window.fill("black")

    current_time = pygame.time.get_ticks()
    if current_time - last_time >= 2000:
        create_chipmunk()
        chipmunk_rand_move()
        last_time = current_time

    player = pygame.draw.rect(window, "blue", (player.x,player.y, 24,24))
    for wall in walls:
        pygame.draw.rect(window, "red", wall)
    for chipmunk in chipmunks:
        pygame.draw.rect(window, "green", chipmunk)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_dir_y[1] = 1
            elif event.key == pygame.K_s:
                player_dir_y[0] = 1

            if event.key == pygame.K_d:
                player_dir_x[1] = 1
            elif event.key == pygame.K_a:
                player_dir_x[0] = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_dir_y[1] = 0
            if event.key == pygame.K_s:
                player_dir_y[0] = 0
                
            if event.key == pygame.K_a:
                player_dir_x[0] = 0
            if event.key == pygame.K_d:
                player_dir_x[1] = 0
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    player_collide()
    
    for chipmunk in range(len(chipmunks)):
        chipmunks_collide(chipmunks[chipmunk], chipmunk, directions[chipmunk][0],directions[chipmunk][1])

    pygame.key.set_repeat(10, 10)
    pygame.display.update()
    pygame.time.Clock().tick(60)
