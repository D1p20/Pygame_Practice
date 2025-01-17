import pygame
import sys
import os

#intialize pygame
pygame.init()

#constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sound and Effects")
SCREEN.fill(BLUE)
#VAR
running = True


#load sounds
music_wav_path = os.path.join("assets", "music.wav")
sound_one_wav_path = os.path.join("assets", "sound_1.wav")
sound_two_wav_path = os.path.join("assets", "sound_2.wav")
sound_one = pygame.mixer.Sound(sound_one_wav_path)
sound_two = pygame.mixer.Sound(sound_two_wav_path)
#ssound_one.set_volume(0.5)
#bg music
pygame.mixer.music.load(music_wav_path)
pygame.mixer.music.play(-1, 0.0, 5000)

while running:
    SCREEN.fill(BLUE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # play sounds
            pygame.mixer.music.stop()
            pygame.time.delay(5000)
            sound_one.play()
            pygame.time.delay(3000)
            running = False
    pygame.display.update()




pygame.quit()
sys.exit()
