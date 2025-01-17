import sys
import os
import pygame


pygame.init()

BLUE = (0, 0, 255, 255)
WHITE = (255, 255, 255, 255)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
SCREEN.fill(BLUE)
pygame.display.set_caption("Blitting Images")

running = True



left_dragon = pygame.image.load(os.path.join("assets", "dragon_left.png")).convert_alpha()
left_dragon_rect = left_dragon.get_rect()
left_dragon_rect.topleft = (0,0)


right_dragon = pygame.image.load(os.path.join("assets", "dragon_right.png")).convert_alpha()
right_dragon_rect = right_dragon.get_rect()
right_dragon_rect.topright = (SCREEN_WIDTH,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    SCREEN.blit(left_dragon, left_dragon_rect)
    SCREEN.blit(right_dragon, right_dragon_rect)
    pygame.draw.line(SCREEN,WHITE,(0,75),(SCREEN_WIDTH,75),4)
    pygame.display.update()
pygame.quit()
sys.exit()