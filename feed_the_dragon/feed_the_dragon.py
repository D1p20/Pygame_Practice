import os.path
import sys
import random
import pygame


#init pygame
pygame.init()
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Dragon")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "dragon_right.png")))



#set fps and clock
FPS = 60
CLOCK = pygame.time.Clock()



#set constants
PLAYER_STARTING_LIVES = 3
PLAYER_VELOCITY = 10
COIN_START_VELOCITY = 10
COIN_ACCELARATION = 1
BUFFER_DISTANCE = 500

score = 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_START_VELOCITY


#colors
GREEN = (0, 255, 0)
DARK_GREEN = (150, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)



"""******** FONTS AND TEXTS *******"""
#fonts
FONT = pygame.font.Font((os.path.join("assets", "AttackGraffiti.ttf")), 40)

#set text
score_text = FONT.render("Score: " + str(score), True, GREEN, DARK_GREEN)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)

#titletext
title_text = FONT.render("Feed the Dragon", True, GREEN, WHITE)
title_text_rect = title_text.get_rect()
title_text_rect.centerx  = SCREEN.get_width() // 2
title_text_rect.y = 10

#lives text
lives = FONT.render("Lives: " + str(player_lives), True, WHITE, DARK_GREEN)
lives_rect = lives.get_rect()
lives_rect.topright = (WINDOW_WIDTH -10, 10)

#gameover text
game_over_text = FONT.render("Game Over", True, WHITE, DARK_GREEN)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

#countinue text
continue_text = FONT.render("PRESS ANY KEY TO PLAY AGAIN", True, WHITE, DARK_GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2)+48)



"""******** SOUNDS AND MUSIC *******"""
coin_sound = pygame.mixer.Sound(os.path.join("assets", "coin_sound.wav"))
miss_sound = pygame.mixer.Sound(os.path.join("assets", "miss_sound.wav"))
miss_sound.set_volume(0.1)

#bg music
pygame.mixer.music.load(os.path.join("assets", "ftd_background_music.wav"))
 
 
"""******** SPRITES *******"""
player_image = pygame.image.load(os.path.join("assets", "dragon_right.png"))
player_image_rect = player_image.get_rect()
player_image_rect.left = 32
player_image_rect.centery = (WINDOW_HEIGHT//2)
 
coin_image = pygame.image.load(os.path.join("assets", "coin.png"))
coin_image_rect = coin_image.get_rect()
coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_image_rect.y = random.randrange(64, WINDOW_HEIGHT-32)


"""******** MAIN LOOP *******"""
running = True
pygame.mixer.music.play(-1, 0.0)
while running:
	SCREEN.fill(BLACK)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#player movement
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		pass
	if keys[pygame.K_RIGHT]:
		pass
	if (keys[pygame.K_UP] or  keys[pygame.K_w]) and player_image_rect.top > 64:
		player_image_rect.y -= PLAYER_VELOCITY
	if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_image_rect.bottom < WINDOW_HEIGHT:
		player_image_rect.y += PLAYER_VELOCITY
	
	#coin movement
	if coin_image_rect.x < 0:
		player_lives -= 1
		miss_sound.play()
		coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
		coin_image_rect.y = random.randrange(64, WINDOW_HEIGHT-32)
	else:
		coin_image_rect.x -= coin_velocity
	if player_image_rect.colliderect(coin_image_rect):
		score += 1
		coin_velocity += COIN_ACCELARATION
		coin_sound.play()
		coin_image_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
		coin_image_rect.y = random.randrange(64, WINDOW_HEIGHT-32)
	
	
	#display texts
	SCREEN.blit(score_text, score_text_rect)
	SCREEN.blit(title_text, title_text_rect)
	SCREEN.blit(lives, lives_rect)
	pygame.draw.line(SCREEN, GREEN, (0,64), (WINDOW_WIDTH,64), 2)
	
	#update texts
	score_text = FONT.render("Score: " + str(score), True, GREEN, DARK_GREEN)
	lives = FONT.render("Lives: " + str(player_lives), True, WHITE, DARK_GREEN)
	
	
	#display images
	SCREEN.blit(player_image, player_image_rect)
	SCREEN.blit(coin_image, coin_image_rect)
	
	# game over
	if player_lives <= 0:
		SCREEN.blit(game_over_text, game_over_rect)
		SCREEN.blit(continue_text, continue_text_rect)
		pygame.display.update()
		pygame.mixer.music.stop()
		is_paused = True
		while is_paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					is_paused = False
					running = False
				elif event.type == pygame.KEYDOWN:
					score = 0
					player_lives = PLAYER_STARTING_LIVES
					player_image_rect.y = WINDOW_HEIGHT//2
					coin_velocity = COIN_START_VELOCITY
					pygame.mixer.music.play(-1, 0.0)
					is_paused = False
		
	pygame.display.update()
	CLOCK.tick(FPS)
pygame.quit()
sys.exit()
