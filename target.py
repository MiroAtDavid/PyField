import pygame
BLACK = (0, 0, 0)

class Target(pygame.sprite.Sprite):
	# This class represents an Enemy. It derives from the 'Sprite' class in Pygame.

	def __init__(self, color, width, height):
		# Call the parent class (Sprite) constructor
		super().__init__()

		# Pass in the color of the brick, and its x and y position, width and height.
		# Set the background color and set it to be transpartent
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		#self.image.set_colorkey(BLACK)

		# Draw the brick (a rectangle)
		#pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.image = pygame.image.load("images/ball10.png").convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)

		# Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()
