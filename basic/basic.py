import sys

import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((640,320))
pygame.display.set_caption("Hello")
#rgb colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255 ,0)
BLUE = (0,0,25)
YELLOW =(255,255,0)
SCREEN.fill(YELLOW)
pygame.draw.line(SCREEN,GREEN,(0,0),(100,100),100)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    pygame.display.update()