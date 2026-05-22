import pygame

from settings import *
from ray_casting import ray_casting

class Drawing:
	def __init__(self, sc):
		self.sc = sc
		self.textures = {'1': pygame.image.load("textures/wall.jpg").convert(), 
						'2': pygame.image.load("textures/2.jpg").convert(),
						's': pygame.image.load("textures/sky.png").convert()}

	def background(self, angle):
		sky_offset = -5 * math.degrees(angle) % WIDTH
		self.sc.blit(self.textures['s'], (sky_offset, 0))
		self.sc.blit(self.textures['s'], (sky_offset - WIDTH, 0))
		self.sc.blit(self.textures['s'], (sky_offset + WIDTH, 0))
		pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

	def world(self, world_objects):
		for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
			if obj[0]:
				_, object, object_pos = obj
				self.sc.blit(object, object_pos)