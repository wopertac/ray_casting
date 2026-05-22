import pygame

class Enemy():
	def __init__(self, x, y, texture):
		self.x = x
		self.y = y
		self.texture = pygame.transform.scale(pygame.image.load("textures/" + texture + ".png"), (900, 900*1.0666666666666667))
		self.rect_texture = self.texture.get_rect()
		self.rect_texture.x = 0
		self.rect_texture.y = 0
		self.drawed = False


	def draw(self, x, y, Wx, sc, x2, y2):
		if not self.drawed:
			pygame.draw.rect(sc, (255, 255, 255), (x, y, Wx, Wx*1.0666666666666667))
			self.drawed = True