import os.path
import sys

import pygame

pygame.init()

SCREEN = pygame.display.set_mode((640,480))
pygame.display.set_caption("Discrete Keyboard Movement")
SCREEN.fill((0,0,255))
running = True

VELOCITY = 10
dragon_image = pygame.image.load(os.path.join("assets", "dragon_left.png")).convert_alpha()
dragon_rect = dragon_image.get_rect()
dragon_rect.centerx = 640//2
dragon_rect.bottom = 470

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dragon_rect.x -= VELOCITY
            if event.key == pygame.K_RIGHT:
                dragon_rect.x += VELOCITY
            if event.key == pygame.K_UP:
                dragon_rect.y -= VELOCITY
            if event.key == pygame.K_DOWN:
                dragon_rect.y += VELOCITY



    pygame.display.update()
    SCREEN.fill((0,0,255))
    SCREEN.blit(dragon_image, dragon_rect)
pygame.quit()
sys.exit()
