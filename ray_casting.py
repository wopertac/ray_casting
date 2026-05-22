import pygame
import math

from settings import *
from map import world_map, world_map2, colors, world_map3, next_lvl

def mapping(a, b):
	return (a // TITLE) * TITLE, (b // TITLE) * TITLE

def ray_casting(player, textures):
	walls = []
	ox, oy = player.pos()
	xm, ym = mapping(ox, oy)
	cur_angle = player.angle - HALF_FOV
	for ray in range(NUM_RAYS):
		sin_a = math.sin(cur_angle)
		cos_a = math.cos(cur_angle)
		color2 = '1'
		texture_h = '1'
		texture_v = '1'

		#verticals
		x, dx = (xm + TITLE, 1) if cos_a >= 0 else (xm, -1)
		for i in range(0, WIDTH, TITLE):
			depth_v = (x - ox) / cos_a
			yv = oy + depth_v * sin_a
			tile_v = mapping(x + dx, yv)
			if tile_v in world_map:
				texture_v = world_map[tile_v]
				break
			x +=  dx * TITLE

		#horizontals
		y, dy = (ym + TITLE, 1) if sin_a >= 0 else (ym, -1)
		for i in range(0, HEIGHT, TITLE):
			depth_h = (y - oy) / sin_a
			xh = ox + depth_h * cos_a
			tile_h = mapping(xh, y + dy)
			if tile_h in world_map:
				texture_h = world_map[tile_h]
				break
			y += dy * TITLE

		#projection
		depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
		offset = int(offset) % TITLE
		depth *= math.cos(player.angle - cur_angle)
		depth = max(depth, 0.0001)
		proj_height = min(int(PROJ_COEFF / depth), 2 * HEIGHT)

		wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
		wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))

		wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
		walls.append((depth, wall_column, wall_pos))

		cur_angle += DELTA_ANGLE
	return walls