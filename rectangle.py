import sys

import pygame


#   clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My PyGame")
fill_color = (32, 52, 71)
step = 10
rect_y = 1
rect_x = 1

screen.fill((255, 0, 0))
rect_color = pygame.Color('lightyellow')

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rect_y >= step:
                rect_y -= step
            if event.key == pygame.K_DOWN and rect_y <= 600 - step - 100:
                rect_y += step
            if event.key == pygame.K_LEFT and rect_x >= step:
                rect_x -= step
            if event.key == pygame.K_RIGHT and rect_x <= 800 - 100 - step:
                rect_x += step

    screen.fill(fill_color)  # pygame.Color('yellow')
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, 100, 100))
    pygame.display.update()

    #   clock.tick((3))
