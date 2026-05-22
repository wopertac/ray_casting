import pygame
import math
import time
import generate

from settings import *
from player import Player
from map import world_map, world_map2, colors, world_map3, update_map, set_lvl
from ray_casting import ray_casting
from random import randint
from drawing import Drawing
from sprite_object import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)
sprites = Sprites()

mini_map = False

f = pygame.font.Font('font.ttf', 36)

player_speed = 10
x = 1
counter = 0
start_time = time.time()
fps_now = 0

text_console = ""
console_activate = False

import mods_load as ml
ml.load_mods()

while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_q:
				if mini_map:
					mini_map = False
				else:
					mini_map = True
			if i.key == pygame.K_ESCAPE:
				exit()

	if (time.time() - start_time) != 0:
		fps_now = int(1.0 / (time.time() - start_time))

	start_time = time.time()

	player.movement()
	sc.fill(BLACK)
	drawing.background(player.angle)

	walls = ray_casting(player, drawing.textures)
	drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
	update_map(player)


	if console_activate:
		console = pygame.Surface((1300, 100))
		console.set_alpha(128)
		console.fill((120, 120, 120))
		sc.blit(console, (0, 0))
		console_render = f.render(text_console, True, (255, 255, 255))
		sc.blit(console_render, (10, 35))

	if mini_map:
		pygame.draw.circle(sc, GREEN, (int(player.x / 10), int(player.y / 10)), 1.2)
		for x,y in world_map:
			pygame.draw.rect(sc, BLUE, (x / 10, y / 10, TITLE / 10, TITLE / 10))
		for x,y in world_map2:
			pygame.draw.rect(sc, BLUE, (x / 10, y / 10, TITLE / 10, TITLE / 10))
		for x, y in world_map3:
			pygame.draw.rect(sc, BLUE, (x / 10 + TITLE // 20, y / 10 + TITLE // 20, COLLUM / 10, COLLUM / 10))

	fps_render = f.render(str(fps_now), True, (0, 255, 255))
	sc.blit(fps_render, (1160, 10))

	pygame.display.flip()
	clock.tick(FPS)