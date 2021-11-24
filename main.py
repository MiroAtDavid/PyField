import pygame
from pygame.locals import *
from gun import Gun
from target import Target
from amunition import Amunition
from random import randint
#import pygame_menu

pygame.init()
# Add some background music
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
#pygame.mixer.music.load('sounds/battle.mp3')
#pygame.mixer.music.play(-1) # -1 means loops for ever, 0 means play just once
# Define some colors
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GREY = (192, 192, 192)
BLACK = (0,0,0)

# Score counter (Targets shot)
score = 0
lives = 3

# Background Picture
# background = pygame.image.load('images/background.jpg')
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
# Draw window
#size = ((1200, 800), pygame.RESIZABLE)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('PyField')

# This will be alist that will contain all the sprites we intend to use.
all_sprites_list = pygame.sprite.Group()
all_targets = pygame.sprite.Group()

# Draw Aim Cross # old but still needed for shooting
gun = Gun(WHITE, 5,5)

# Create the bullet and target sprite
bullet = Amunition(WHITE, 1, 1)
target = Target

# Simple for now , add random timing, popups and movement.
def level_one(color, asize, bsize, x, y):
	target = Target(color,asize,bsize)
	target.rect.x = x
	target.rect.y = y
	oldposx = target.rect.x
	oldposy = target.rect.y
	all_sprites_list.add(target)
	all_targets.add(target)

def check(target, all_targets):
	if pygame.sprite.spritecollideany(target, all_targets):
		return True
	else:
		for entitiy in all_targets:
			if entitiy == target:
				if (abs(target.rect.x - entitiy.rect.x) < 25 and (abs(target.rect.y - entitiy.rect.y)) < 25):
					return True
		return False

colorlist = [GREY, ORANGE, LIGHTBLUE, DARKBLUE, YELLOW, RED]

tar1 = level_one(colorlist[randint(0,5)], 10,10, randint(600,800),randint(400,600))
tar2 = level_one(colorlist[randint(0,5)], 10,10, randint(600,800),randint(400,600))
tar3 = level_one(colorlist[randint(0,5)], 10,10, randint(600,800),randint(400,600))
tar4 = level_one(colorlist[randint(0,5)], 10,10, randint(600,800),randint(400,600))
tar5 = level_one(colorlist[randint(0,5)], 10,10, randint(600,800),randint(400,600))
tar6 = level_one(colorlist[randint(0,5)], 10,10, randint(600,800),randint(400,600))

starget = [tar1, tar1, tar1 ,tar1 ,tar1 ,tar1]

#pygame.display.quit()
#pygame.quit()
# Add the gun to the list of sprites
all_sprites_list.add(gun)

# The loop will carry on until the user exits the game
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
#pygame.mouse.set_visible(True)
pygame.mouse.set_cursor(3)
start_ticks = pygame.time.get_ticks() #starter tick
mouseClick = 0

#-------------Main Programm loop.................#

while carryOn:

	# User did something
	# Searching still for ways not to get balls pop up over existing balls
	for event in pygame.event.get():
		newposx = randint(300, 900)
		newposy = randint(200, 600)

		# Exit Game
		if event.type == pygame.QUIT:
			carryOn = False

		# Shoot'em up
		if event.type == pygame.MOUSEBUTTONDOWN:
			shot = gun.mouse_shoot()
			Mouse = pygame.mouse.get_pos()
			bullet.rect.x = (Mouse[0]//1)*1
			bullet.rect.y = (Mouse[1]//1)*1
			all_sprites_list.add(bullet)
			bullet.kill()
			mouseClick += 1

		# Add target after hit
		if check != True:
			if len(all_targets) == 5:
				all_sprites_list.add(target)
				all_targets.add(target)
				target.rect.x = newposx
				target.rect.y = newposy

	# Calculate Seconds
	seconds=(pygame.time.get_ticks()-start_ticks)/1000
	#screen.blit(MANUAL_CURSOR, (pygame.mouse.get_pos()))

	# Background
	screen.fill(WHITE)
	#screen.blit(background, (0,0))

	# Game logic should go here
	all_sprites_list.update()

	# Check if the gun colides with any of the targets
	target_collisoin_list = pygame.sprite.spritecollide(bullet, all_targets, False, pygame.sprite.collide_mask)
	for target in target_collisoin_list:
		effect = pygame.mixer.Sound('sounds/blop.mp3')
		effect.play()
		score += 1
		target.kill()
		bullet.kill()

	# No targets left, level complete.
	# if len(all_targets) == 0:
	# 60 sec Timer for level
	if seconds > 60:
		# Display Level Message for 3 seconds
		font = pygame.font.Font(None, 74)
		text = font.render("LEVEL COMPLETE", 1, BLACK)
		screen.blit(text, (200,300))
		font = pygame.font.Font(None, 74)
		text = font.render("Score: " +str(score), 1, BLACK)
		screen.blit(text, (200,400))

		# Cals hit/miss ratio
		hitratio = score / mouseClick * 100
		font = pygame.font.Font(None, 74)
		text = font.render("Precission (%): " +str(hitratio), 1, BLACK)
		screen.blit(text, (200,500))
		pygame.display.flip()
		pygame.time.wait(4000)
		pygame.display.flip()

		#carryOn=False

	# --- Drawing code should go here
	pygame.draw.line(screen, BLACK, [0, 38], [1200, 38], 1)
	pygame.draw.line(screen, BLACK, [0, 762], [200, 668], 1)
	pygame.draw.line(screen, BLACK, [0, 38], [200, 132], 1)
	pygame.draw.line(screen, BLACK, [1200, 762], [1000, 668], 1)
	pygame.draw.line(screen, BLACK, [1200, 38], [1000, 132], 1)
	pygame.draw.rect(screen,BLACK, [200, 132, 800, 536], 1)

	# Display the score and the number of lives at the top of the screen
	font = pygame.font.Font(None, 24)
	text = font.render("Score: " +str(score), 1, BLACK)
	screen.blit(text, (20, 10))

    #Now let's draw all the sprites in one go. (For now we have only 2 sprites!)
	all_sprites_list.draw(screen)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
