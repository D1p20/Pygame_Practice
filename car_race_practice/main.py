import pygame
import sys
import os

pygame.init()

# Screen setup
SIZE = width, height = 480, 720
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Car Race")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "car.png")))

# Define colors
ROAD_GREY = (105, 105, 105)
GRASS_GREEN = (34, 139, 34)

# Bools
is_fullscreen = True
running = True
paused = False

# Draw road dimensions
road_width = 400
road = pygame.Rect(0, 0, road_width, pygame.display.Info().current_h)
road.center = (pygame.display.Info().current_w // 2, pygame.display.Info().current_h // 2)

# Draw road separator
separator = pygame.image.load(os.path.join("assets", "yellow_line.png")).convert_alpha()
separator_rect = separator.get_rect()
separator_rect.center = road.center

separator_rect_copy = separator.get_rect()
separator_rect_copy.centerx = road.centerx
separator_rect_copy.bottom = separator_rect.top


# Speed for scrolling the separator
separator_speed = 2

# main loop control
FPS = 60
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_f:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    road.height = pygame.display.Info().current_h
                else:
                    screen = pygame.display.set_mode(SIZE)
                    road.height = height
                road.center = (pygame.display.Info().current_w // 2, pygame.display.Info().current_h // 2)
                separator_rect.centerx = road.centerx
                separator_rect_copy.centerx = road.centerx

    # Fill background with grass green
    screen.fill(GRASS_GREEN)

    # Draw the road
    pygame.draw.rect(screen, ROAD_GREY, road)

    # Draw separator
    separator_rect.y += separator_speed
    separator_rect_copy.y += separator_speed
    screen.blit(separator, separator_rect)
    screen.blit(separator, separator_rect_copy)

    # Reset separator position for seamless scrolling
    if separator_rect.top >= pygame.display.Info().current_h:
        separator_rect.bottom = separator_rect_copy.top
    if separator_rect_copy.top >= pygame.display.Info().current_h:
        separator_rect_copy.bottom  = separator_rect.top

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
