import pygame
import random,os,sys


pygame.init()


#screen setup
SCREEN_WIDTH = 945
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Clown")
pygame.display.set_icon(pygame.image.load(os.path.join("assets", "clown.png")))


#set game values
PLAYER_START_LIVES = 5
CLOWN_START_SPEED = 3
CLOWN_ACCELARATION = 0.5

_score = 0
_player_lives = PLAYER_START_LIVES
_clown_speed = CLOWN_START_SPEED
_clown_delta_x = random.choice([-1,1])
_clown_delta_y = random.choice([-1,1])


#set colors
BLUE = (1, 175, 209)
YELLOW = (248,231,28)
WHITE = (255,255,255)


#set fonts
font = pygame.font.Font(os.path.join("assets", "Franxurter.ttf"), 32)

#set texts
score_text =font.render("Score: " + str(_score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (SCREEN_WIDTH - 50, 10)


title_text = font.render("Catch the Clown", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50,10)

lives_text = font.render("Lives: " + str(_player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (SCREEN_WIDTH - 50, 50)

game_over_text = font.render("Game Over", True, WHITE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

continue_text = font.render("Click anywhere to play again", True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2)+64)

#set sound and music
click_sound = pygame.mixer.Sound(os.path.join("assets", "click_sound.wav"))
click_sound.set_volume(0.1)
miss_sound = pygame.mixer.Sound(os.path.join("assets", "miss_sound.wav"))
miss_sound.set_volume(0.1)
pygame.mixer.music.load(os.path.join("assets", "ctc_background_music.wav"))

#set images
background_image = pygame.image.load(os.path.join("assets", "background.png"))
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

clown_image = pygame.image.load(os.path.join("assets", "clown.png"))
clown_rect = clown_image.get_rect()
clown_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#running variable
clock = pygame.time.Clock()
FPS = 60
running = True

#mainloop
pygame.mixer.music.play(-1, 0.0)
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if clown_rect.collidepoint(event.pos[0], event.pos[1]):
				click_sound.play()
				_clown_speed += CLOWN_ACCELARATION
				previous_delta_x = _clown_delta_x
				previous_delta_y = _clown_delta_y
				while previous_delta_x == _clown_delta_x and previous_delta_y == _clown_delta_y:
					_clown_delta_x = random.choice([-1, 1])
					_clown_delta_y = random.choice([-1, 1])
				_score += 1
			else:
				miss_sound.play()
				_player_lives -= 1
				
	
	#move clown
	clown_rect.x += _clown_delta_x  * _clown_speed
	clown_rect.y += _clown_delta_y * _clown_speed

	if clown_rect.left <= 0 or clown_rect.right >= SCREEN_WIDTH:
		_clown_delta_x *= -1
	if clown_rect.top <= 0 or clown_rect.bottom >= SCREEN_HEIGHT:
		_clown_delta_y *= -1
	
	#blit bg
	screen.blit(background_image, background_rect)
	#hud
	screen.blit(title_text, title_rect)
	screen.blit(lives_text, lives_rect)
	screen.blit(score_text, score_rect)
	
	#player_image
	screen.blit(clown_image, clown_rect)
	#update hud
	lives_text = font.render("Lives: " + str(_player_lives), True, YELLOW)
	score_text = font.render("Score: " + str(_score), True, YELLOW)
	if _player_lives == 0:
		screen.blit(game_over_text, game_over_rect)
		screen.blit(continue_text, continue_rect)
		pygame.display.update()
		
		#pause
		pygame.mixer.music.stop()
		is_paused = True
		while is_paused:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					is_paused = False
					running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					_score = 0
					_player_lives = PLAYER_START_LIVES
					clown_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
					_clown_speed = CLOWN_START_SPEED
					_clown_delta_x = random.choice([-1, 1])
					_clown_delta_y = random.choice([-1, 1])
					pygame.mixer.music.play(-1, 0.0)
					is_paused = False
					
	pygame.display.update()
	clock.tick(FPS)
pygame.quit()
sys.exit()
