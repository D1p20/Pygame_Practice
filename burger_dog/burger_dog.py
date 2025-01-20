import pygame
import os
import random
import sys


# Initialize pygame
pygame.init()

# Game values
DOG_START_LIVES = 3
DOG_START_SCORE = 0
DOG_START_SPEED = 5
BURGER_START_SPEED = 4
ACCELERATION = 0.25

lives = DOG_START_LIVES
score = DOG_START_SCORE
speed = DOG_START_SPEED
speed_burger = BURGER_START_SPEED
acceleration = ACCELERATION

WINDOW = WIDTH, HEIGHT = 640, 480
FULL_SCREEN = F_WIDTH, F_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((F_WIDTH, F_HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=1)
pygame.mouse.set_visible(False)
pygame.display.set_caption("Burger Dog")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "dog_left.png")))

# Set colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set font
font = pygame.font.Font(os.path.join("assets", "WashYourHand.ttf"), 36)

# Set text
lives_text = font.render("Lives: " + str(lives), True, WHITE)
score_text = font.render("Score: " + str(score), True, WHITE)
game_over_text = font.render("Game Over", True, WHITE)
continue_text = font.render("PRESS SPACE TO PLAY AGAIN", True, WHITE)

# Set images
dog_left = pygame.image.load(os.path.join("assets", "dog_left.png"))
dog_right = pygame.image.load(os.path.join("assets", "dog_right.png"))
current_dog = dog_left
dog_rect = dog_left.get_rect()
dog_rect.center = (F_WIDTH // 2, F_HEIGHT // 2)

burger = pygame.image.load(os.path.join("assets", "burger.png"))
burger_rect  = burger.get_rect()
burger_rect.center = (random.randint(0, F_WIDTH-burger_rect.width), (burger_rect.width+10)*-1)

#set music
score_sound = pygame.mixer.Sound(os.path.join("assets", "bark_sound.wav"))
score_sound.set_volume(0.1)

miss_sound = pygame.mixer.Sound(os.path.join("assets", "miss_sound.wav"))
miss_sound.set_volume(0.1)

pygame.mixer.music.load(os.path.join("assets", "bd_background_music.wav"))
pygame.mixer.music.set_volume(0.1)

# Main loop
running = True
is_paused = False
is_fullscreen = True
FPS = 60
clock = pygame.time.Clock()
pygame.mixer.music.play(-1, 0.0)
boost_counter = 0
is_boosted = False
start_time =0
while running:
    current_width = pygame.display.Info().current_w
    current_height = pygame.display.Info().current_h

    # Update dog direction based on position
    if dog_rect.centerx > current_width // 2:
        current_dog = dog_right
    else:
        current_dog = dog_left

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_f:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(WINDOW)
                    
                current_width = pygame.display.Info().current_w
                current_height = pygame.display.Info().current_h
                dog_rect.center = (current_width // 2, current_height // 2)
                burger_rect.center = (random.randint(0, current_width - burger_rect.width), (burger_rect.width + 10) * -1)
                

    # Handle movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dog_rect.x > 0:
        dog_rect.x -= speed
        current_dog = dog_left
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dog_rect.x < current_width - dog_rect.width:
        dog_rect.x += speed
        current_dog = dog_right
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dog_rect.y > 0:
        dog_rect.y -= speed
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dog_rect.y < current_height - dog_rect.height:
        dog_rect.y += speed
    
    # Render screen
    screen.fill(BLUE)

    # Show player
    screen.blit(current_dog, dog_rect)
    #show and move burger
    screen.blit(burger, burger_rect)
    burger_rect.y += speed_burger + acceleration
    if burger_rect.top > current_height:
        burger_rect.center =(random.randint(0, current_width - burger_rect.width), (burger_rect.width + 10) * -1)
        miss_sound.play()
        lives -= 1
        lives_text = font.render("Lives: " + str(lives), True, WHITE)

    #check collision
    if dog_rect.colliderect(burger_rect):
        burger_rect.center = (random.randint(0, current_width - burger_rect.width), (burger_rect.width + 10) * -1)
        score += 1
        boost_counter += 1
        score_text = font.render("Score: " + str(score), True, WHITE)
        acceleration += .25
        score_sound.play()
    if boost_counter == 10 and is_boosted == False:
        start_time = pygame.time.get_ticks()
        is_boosted = True
        speed += 50
    if is_boosted:
        if pygame.time.get_ticks() - start_time > 10000:
            boost_counter = 0
            speed -= 50
            is_boosted = False
    
    # Show HUD
    screen.blit(lives_text, (current_width - 150, 30))
    screen.blit(score_text, (current_width - 150, 70))
    
    if lives <= 0:
        is_paused = True
        is_game_over_shown = False
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    is_paused = False
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        is_paused = False
                    elif event.key == pygame.K_SPACE:
                        is_paused = False
                        pygame.mixer.music.play(-1, 0.0)
            pygame.mixer.music.stop()
            screen.fill(RED)
            if not is_game_over_shown :
                lives_text = font.render("Lives: " + str("0"), True, WHITE)
                screen.blit(lives_text, (current_width - 150, 30))
                screen.blit(score_text, (current_width - 150, 70))
                screen.blit(game_over_text, (current_width // 2 - game_over_text.get_width() // 2, current_height // 2 - game_over_text.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                lives = DOG_START_LIVES
                score = DOG_START_SCORE
                speed = DOG_START_SPEED
                speed_burger = BURGER_START_SPEED
                acceleration = ACCELERATION
                dog_rect.center = (current_width // 2, current_height // 2)
                lives_text = font.render("Lives: " + str(lives), True, WHITE)
                score_text = font.render("Score: " + str(score), True, WHITE)
                is_game_over_shown = True
            else:
                screen.blit(continue_text, (current_width // 2 - continue_text.get_width() // 2, current_height // 2 - continue_text.get_height() // 2))
            pygame.display.flip()
                    

    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
