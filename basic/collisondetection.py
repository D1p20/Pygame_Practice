import pygame
import sys
import os
import random


pygame.init()
# constants
VELOCITY = 5
WIN_HEIGHT = 600
WIN_WIDTH = 800
SCREEN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Collision Detection")

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# images

dragon_right = pygame.image.load(os.path.join("assets", "dragon_right.png")).convert_alpha()
dragon_right_rect = dragon_right.get_rect()
dragon_right_rect.center  = (25,25)

coin_image = pygame.image.load(os.path.join("assets", "coin.png")).convert_alpha()
coin_rect = coin_image.get_rect()
coin_rect.center = (WIN_WIDTH/2, WIN_HEIGHT/2)

#fps
FPS = 60
CLOCK = pygame.time.Clock()


# var
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Get the state of all the keys (whether they are pressed or not)
    keys = pygame.key.get_pressed()
    # Check if the left arrow key is pressed, move the dragon left
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_right_rect.x > 0:
        dragon_right_rect.x -= VELOCITY
    # Check if the right arrow key is pressed, move the dragon right
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_right_rect.x < WIN_WIDTH - dragon_right_rect.width:
        dragon_right_rect.x += VELOCITY
    # Check if the up arrow key is pressed, move the dragon up
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_right_rect.y > 0:
        dragon_right_rect.y -= VELOCITY
    # Check if the down arrow key is pressed, move the dragon down
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_right_rect.y < WIN_HEIGHT - dragon_right_rect.height:
        dragon_right_rect.y += VELOCITY

    #collsion check
    if dragon_right_rect.colliderect(coin_rect):

        coin_rect.left = random.randint(0, WIN_WIDTH -32)
        coin_rect.top = random.randint(0, WIN_HEIGHT -32)
    SCREEN.fill(BLUE)
    pygame.draw.rect(SCREEN, RED, dragon_right_rect, 1)
    SCREEN.blit(dragon_right, dragon_right_rect)


    SCREEN.blit(coin_image, coin_rect)
    pygame.draw.rect(SCREEN, GREEN, coin_rect, 1)
    pygame.display.update()
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
