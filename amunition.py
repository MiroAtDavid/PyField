import pygame
from random import randint
BLACK = (0, 0, 0)

class Amunition(pygame.sprite.Sprite):
	# This class represents a ball. It derives from the "Sprite" class in Pygame.

	def __init__(self, color, width, height):
		# Call the parent class (Sprite) consctructor
		super().__init__()

		# Pass in the color of the ball, its width and height.
		# Set the background color and set it to be transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		# Draw the ball (a rectangle!)
		pygame.draw.rect(self.image, color, [0, 0, width, height])


		#self.image = pygame.image.load("images/ball.png").convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)
		self.velocity = [randint(0,0), randint(0,0)]


		# Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = -randint(-0, 0)
