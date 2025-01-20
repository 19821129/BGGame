import pygame, sys
from random import *
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

WINDOW = pygame.display.set_mode((900, 700))
pygame.display.set_caption('UpgBG-OS SnakeGame')
surface = pygame.display.set_mode((900,700))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 0, 0)
RED = pygame.Color(255, 255, 0)

snake_position = [100, 50]
snake_body = [[100, 50]]

food_position = [300, 150]
food_spawn = True

direction = 'RIGHT'
change_to = direction

def game_over():
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            if event.key == K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if change_to == 'RIGHT':
        direction = 'RIGHT'
    if change_to == 'LEFT':
        direction = 'LEFT'
    if change_to == 'UP':
        direction = 'UP'
    if change_to == 'DOWN':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        snake_body.insert(0, list(snake_position))
        snake_body.insert(0, list(snake_position))
        snake_body.insert(0, list(snake_position))
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_position = [randint(0, 39) * 10, randint(0, 29) * 10]
    food_spawn = True
    WINDOW.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(WINDOW, RED, pygame.Rect(
            pos[0], pos[1], 10, 10))
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(
        food_position[0], food_position[1], 10, 10))
    #if snake_position[0] >= 900 or snake_position[0] < 0:
        #game_over()
    #if snake_position[1] >= 700 or snake_position[1] < 0:
        #game_over()
    pygame.display.update()
    fpsClock.tick(11)
