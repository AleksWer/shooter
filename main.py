import sys

import pygame
from random import randint

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My PyGame")

screen.fill((255, 0, 0))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((randint(0, 255), randint(0, 255), randint(0, 255)))  # pygame.Color('yellow')
    pygame.display.update()

    clock.tick((3))
