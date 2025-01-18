import pygame
import os
import sys
import random

# Initialize pygame
pygame.init()

# Set window dimensions and initialize display
WINDOW_SIZE = WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode(WINDOW_SIZE, pygame.NOFRAME)
pygame.display.set_caption("Snake Game")

# Set FPS and clock
FPS = 10
clock = pygame.time.Clock()

# Set game values
SECTION_SIZE = 20

snake_x = WIDTH // 2
snake_y = HEIGHT // 2

snake_velocity_x = 0
snake_velocity_y = -SECTION_SIZE

score = 0

# Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)


# Set fonts
font = pygame.font.SysFont("tahoma", 24)

# Set text
score_text = font.render(f"Score: {score}", True, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

game_over_text = font.render("GAME OVER", True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH // 2, HEIGHT // 2)

continue_text = font.render("PRESS ANY KEY TO PLAY AGAIN", True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WIDTH // 2, HEIGHT // 2 + 50)

# Set sounds and music
pick_up_sound = pygame.mixer.Sound(os.path.join("assets", "pick_up_sound.wav"))
pick_up_sound.set_volume(0.1)

# Initialize snake and food positions
food_position = (50, 50, SECTION_SIZE, SECTION_SIZE)
food_rect = pygame.Rect(food_position)

snake_head = (snake_x, snake_y, SECTION_SIZE, SECTION_SIZE)
snake_rect = pygame.Rect(snake_head)
snake_body = [snake_head,snake_head,snake_head]
color_effect = snake_head
# Main game loop
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Update snake direction based on key press
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if snake_velocity_x == 0:
                    snake_velocity_x = -SECTION_SIZE
                    snake_velocity_y = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if snake_velocity_x == 0:
                    snake_velocity_x = SECTION_SIZE
                    snake_velocity_y = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if snake_velocity_y == 0:
                    snake_velocity_x = 0
                    snake_velocity_y = -SECTION_SIZE
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if snake_velocity_y == 0:
                    snake_velocity_x = 0
                    snake_velocity_y = SECTION_SIZE

    if not game_over:
        # Update snake position
        snake_x += snake_velocity_x
        snake_y += snake_velocity_y
        snake_head = (snake_x, snake_y, SECTION_SIZE, SECTION_SIZE)
        snake_rect = pygame.Rect(snake_head)

        # Check for food
        if snake_rect.colliderect(food_rect):
            score += 1
            pick_up_sound.play()
            snake_body.append(snake_head)

            # Generate a new random position for the food
            food_x = random.randint(0, (WIDTH - SECTION_SIZE) // SECTION_SIZE) * SECTION_SIZE
            food_y = random.randint(0, (HEIGHT - SECTION_SIZE) // SECTION_SIZE) * SECTION_SIZE
            food_position = (food_x, food_y, SECTION_SIZE, SECTION_SIZE)
            food_rect = pygame.Rect(food_position)

        # Update snake body
        snake_body.insert(0, snake_head)
        snake_body.pop()

        # Out-of-bound check
        if snake_x < 0:
            snake_x = WIDTH - SECTION_SIZE
        elif snake_x >= WIDTH:
            snake_x = 0
        if snake_y < 0:
            snake_y = HEIGHT - SECTION_SIZE
        elif snake_y >= HEIGHT:
            snake_y = 0

        # Check for collision with itself
        for body_part in snake_body[1:]:
            if snake_head == body_part:
                color_effect = body_part
                game_over = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw game objects
    pygame.draw.rect(screen, RED, snake_head)
    
    pygame.draw.rect(screen, RED, snake_body[0])
    for body_part in snake_body[1:]:
        pygame.draw.rect(screen, DARK_GREEN, body_part)

    pygame.draw.rect(screen, GREEN, food_position)

    # Display HUD
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, score_rect)

    if game_over:
        screen.blit(game_over_text, game_over_rect)
        colors = [RED, GREEN, DARK_GREEN]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        break
            for color in colors:
                pygame.draw.rect(screen, color, color_effect)
            
        

    # Refresh display
    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame
pygame.quit()
sys.exit()
