import pygame
import random
import sys
import time

screen_x = 540 #              screen width
screen_y = 480 #              screen width
fps = 5
SNAKE_SIZE = 15

cols_x = int(screen_x / SNAKE_SIZE)
cols_y = int(screen_y / SNAKE_SIZE)

x = int((cols_x / 2) * SNAKE_SIZE)
y = int((cols_y / 2) * SNAKE_SIZE)

food_d = SNAKE_SIZE

x_food = random.randint(1, cols_x) * food_d # ranfom food position
y_food = random.randint(1, cols_y) * food_d # ranfom food position

snake_lenght = 1
score = 0

dx = 0 # direction
dy = -1 # direction

pygame.init() # inition
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont("Comic Sans MS", 50) # set font, font size
    font_text = font.render("Game Over", True, pygame.Color("red")) # render text
    screen.blit(font_text, (150, 100)) # draw text

while True:
    screen.fill((0, 0, 0)) # bg
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # exit game
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN: # keyboard event
            if event.key == pygame.K_LEFT:
                dx = -1
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 1
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -1
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 1

    x += int(dx * SNAKE_SIZE)
    y += int(dy * SNAKE_SIZE)

    a = x_food + food_d / 2 # POSITION OF FOOD
    b = y_food + food_d / 2 # POSITION OF FOOD
    
    pygame.draw.rect(screen, (255, 0, 0), [x, y, SNAKE_SIZE, SNAKE_SIZE])
    # pygame.draw.rect(screen, (0, 255, 0), [a, b], food_d / 2) # draw food

    if x > screen_x or x < 0 or y > screen_y or y < 0:
        game_over()
        pygame.display.flip()
        time.sleep(2)
        break
    if x == x_food and y == y_food:
        score += 1
        x_food = random.randint(1, cols_x) * food_d
        y_food = random.randint(1, cols_y) * food_d

    pygame.display.flip()
    clock.tick(fps)