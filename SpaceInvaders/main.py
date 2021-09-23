import pygame

# init pygame
pygame.init()

width = 800
height = 600

# create screen
screen = pygame.display.set_mode((width, height))


# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load('player.png')
player_x = 370
player_y = 480
player_x_change = 0

def player(x,y):
    screen.blit(player_img, (x, y))

# basic gameloop (while true)
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keystroke pressed check right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x -= 0.6
        if event.key == pygame.K_RIGHT:
            player_x += 0.6

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    player(player_x,player_y)
    pygame.display.update()
