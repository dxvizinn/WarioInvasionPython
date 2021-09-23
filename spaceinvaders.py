import pygame
import math
import random

# init pygame
pygame.init()

print('Good luck!')

width = 800
height = 600

# create screen
screen = pygame.display.set_mode((width, height))

# background
background = pygame.image.load('background.jpg')

# title and icon
pygame.display.set_caption('Wario Invasion!')
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

# enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(0.8)
    enemy_y_change.append(65)

# bullet
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 0.9
bullet_state = "ready"

# font and score value
score_value = 0
font = pygame.font.Font('supermario256.ttf',32)

text_x = 10
text_y = 10

# game over text
over_font = pygame.font.Font('supermario256.ttf',40)


def show_score(x, y):
    score = font.render('Warios Defeated: ' + str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render('Wario got the world ):', True, (255,0,0))
    screen.blit(over_text, (120, 250))

def player(x,y):
    screen.blit(player_img, (x, y))

def enemy(x,y,i):
    screen.blit(enemy_img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt((math.pow(enemy_x-bullet_x,2))+ (math.pow(enemy_y-bullet_y,2)))
    if distance <= 27:
        return True
    else:
        return False

# basic gameloop (while true)
running = True
while running:

    # rgb
    screen.fill((0, 0, 0))
    # bg img
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Goodbye!')
            running = False

    # keystroke pressed check right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x -= 0.7
        if event.key == pygame.K_RIGHT:
            player_x += 0.7
        if event.key == pygame.K_UP:
            if bullet_state is "ready":    
                bullet_x = player_x
                fire_bullet(player_x, bullet_y)
        
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            player_x_change = 0

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # q = quit
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_q:
            print('Goodbye!')
            running = False

    # enemy mov
    for i in range(num_of_enemies):

        # game over
        if enemy_y[i] > 440:
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break
        
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.4
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.4
            enemy_y[i] += enemy_y_change[i]


        # collision
        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, 735)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    # bullet mov
    if bullet_y <= 0:
        bullet_y =480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    

    player(player_x,player_y)
    show_score(text_x, text_y)
    pygame.display.update()
