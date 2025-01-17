import pygame
import sys
import os

# Initialize all imported pygame modules
pygame.init()

# Set the frames per second (FPS) for the game
FPS = 60
# Create a clock object to manage how fast the game updates
CLOCK = pygame.time.Clock()

# Define constants for screen size and movement velocity
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
VELOCITY = 5
# Create the game window with the defined width and height
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the caption for the window
pygame.display.set_caption("Mouse Input")

# Define some colors for later use
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load the dragon image and convert it for better performance with transparency handling
dragon_img = pygame.image.load(os.path.join("assets", "dragon_right.png")).convert_alpha()
# Get the rectangle object for the image to handle positioning
dragon_rect = dragon_img.get_rect()
# Set the initial position of the dragon in the center of the screen
dragon_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Variable to control the game loop
running = True

# Start the game loop
while running:
    # Check for all the events in the event queue
    for event in pygame.event.get():
        # If the user clicks the close button on the window
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop
        # If the user clicks the mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the dragon's position to where the mouse was clicked
            dragon_rect.center = (event.pos[0], event.pos[1])
        # If the mouse is being moved and the left button is pressed
        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
            # Update the dragon's position to follow the mouse cursor
            dragon_rect.center = (event.pos[0], event.pos[1])

    # Get the state of all the keys (whether they are pressed or not)
    keys = pygame.key.get_pressed()
    # Check if the left arrow key is pressed, move the dragon left
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and dragon_rect.x > 0:
        dragon_rect.x -= VELOCITY
    # Check if the right arrow key is pressed, move the dragon right
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_rect.x < SCREEN_WIDTH - dragon_rect.width:
        dragon_rect.x += VELOCITY
    # Check if the up arrow key is pressed, move the dragon up
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_rect.y > 0:
        dragon_rect.y -= VELOCITY
    # Check if the down arrow key is pressed, move the dragon down
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_rect.y < SCREEN_HEIGHT - dragon_rect.height:
        dragon_rect.y += VELOCITY

    # Fill the screen with the blue background color
    SCREEN.fill(BLUE)
    # Draw the dragon image on the screen at its current position
    SCREEN.blit(dragon_img, dragon_rect)
    # Update the display to reflect the changes
    pygame.display.update()
    # Tick the clock to maintain the FPS (60 frames per second)
    CLOCK.tick(FPS)

# Quit pygame and close the game window
pygame.quit()
# Exit the program
sys.exit()
