from pygame import *
import main

map = ['o', 'o', 'o', 'o', 'o', 'o', 'o',],['o', 'o', 'o', 'o', 'o', 'o', 'o',],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o',],['o', 'o', 'o', 'o', 'o', 'o', 'o',],['o', 'o', 'o', 'o', 'o', 'o', 'o',],
  ['o', 'o', 'o', 'o', 'o', 'o', 'o',],['o', 'o', 'o', 'o', 'o', 'o', 'o',]

def generation_mao(map):
  for map in j:
    if j == 'o': #                                                                                 create free map
      pygame.draw.rect(main.screen, (0, 255, 0), [0, 0, main.SNAKE_SIZE, main.SNAKE_SIZE])
    if j == 'w': #                                                                                 create a wall
      pygame.draw.rect(main.screen, (255, 0, 0), [0, 0, main.SNAKE_SIZE, main.SNAKE_SIZE])
  
