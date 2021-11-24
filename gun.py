import pygame
from amunition import Amunition
from target import Target
BLACK = (0,0,0)
WHITE = (255, 255, 255)

class Gun(pygame.sprite.Sprite):
	# This class represents the homebase. It derives from the 'Sprite' class in Pygame

	def __init__(self, color, width, height):
		# Call the parent class (Sprite) constructor
		super().__init__()


		# Pass in the color of the homebase, its x and y position, width and height
		# Set the background color and set it to be transparent.
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		# Draw the homebase (a rectangle FOR NOW)
		#pygame.draw.ellipse(self.image, color, [0, 0, width, height], 1)
		#self.image = pygame.image.load('images/basecan.png').convert_alpha()

		# Fetch the rectangle object that has the dimensions of the image
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface(self.image)

	# Mouse movement
	#def mouse_move(self):
	#	self.rect.center= pygame.mouse.get_pos()
	#	pygame.display.update()

	# Mouse button pressed e.g shooting
	def mouse_shoot(self):
		mouse_target = pygame.mouse.get_pressed()
		if mouse_target[0]:
			Mouse = pygame.mouse.get_pos()
			pygame.display.update()
