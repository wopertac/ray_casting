import pygame
import numpy as np
import os

pygame.init()
W, H = 1360, 760
Wl = 30
sc = pygame.display.set_mode((W, H))

map_list = np.zeros((45, 25), dtype=int)

block = 1

def change_block(x, y):
	global map_list
	if (map_list[x][y] == 0) and ((x != 1) or (y != 1)):
		map_list[x][y] = block
	else:
		map_list[x][y] = 0
		# print(map_list[x][y])

while True:
	sc.fill((0, 0, 0))
	for i in pygame.event.get():

		if i.type == pygame.MOUSEBUTTONDOWN:
			if i.button  == 1:
				map_x = i.pos[0] // Wl
				map_y = i.pos[1] // Wl
				if (map_x <= 45) and (map_y <= 25):
					change_block(map_x, map_y)

		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_1:
				block = 1
			if i.key == pygame.K_2:
				block = 2
			if i.key == pygame.K_3:
				block = 3


			if i.key == pygame.K_ESCAPE:
				exit()
			if i.key == pygame.K_p:
				levels = os.listdir("levels")
				levels_2 = os.listdir("new_levels")
				print("save as :", str(len(levels) + 1 + len(levels_2)) + ".txt")
				save = open("levels/" + str(len(levels) + 1 + len(levels_2)) + ".txt", "w+")
				save_text = ""
				save_text += str(25) + "\n"
				for x in range(len(map_list)):
					for y in range(len(map_list[x])):
						if(map_list[x][y] == 0):
							save_text += "."
						elif(map_list[x][y] == 1):
							save_text += "W"
						elif(map_list[x][y] == 2):
							save_text += "P"
						elif(map_list[x][y] == 3):
							save_text += "O"
					save_text += "\n"
				save.write(save_text)
				save.close()

	#draw
	for i in range(0, H, Wl):
		pygame.draw.line(sc, (255, 255, 255), (0, i), ((W // Wl) * Wl, i))
	for j in range(0, W, Wl):
		pygame.draw.line(sc, (255, 255, 255), (j, 0), (j, (H // Wl) * Wl))

	pos_m = pygame.mouse.get_pos()
	m_x = int(pos_m[0] // Wl)
	m_y = int(pos_m[1] // Wl)

	if block == 1:
		surface = pygame.Surface((Wl, Wl))
		surface.fill((245, 194, 66))
		surface.set_alpha(128)
		sc.blit(surface, (m_x * Wl, m_y * Wl))
	if block == 2:
		surface = pygame.Surface((Wl // 2, Wl // 2))
		surface.fill((245, 194, 66))
		surface.set_alpha(128)
		sc.blit(surface, (m_x * Wl + (Wl // 4), m_y * Wl + (Wl // 4)))
	if block == 3:
		surface = pygame.Surface((Wl, Wl))
		surface.fill((255, 0, 0))
		surface.set_alpha(128)
		sc.blit(surface, (m_x * Wl, m_y * Wl))

	for i in range(len(map_list)):
		for j in range(len(map_list[i])):
			if (map_list[i][j] == 1):
				pygame.draw.rect(sc, (245, 194, 66), (i * Wl, j * Wl, Wl, Wl))
			if (map_list[i][j] == 2):
				pygame.draw.rect(sc, (245, 194, 66), (i * Wl + (Wl // 4), j * Wl + (Wl // 4), Wl // 2, Wl // 2))
			if (map_list[i][j] == 3):
				pygame.draw.rect(sc, (255, 0, 0), (i * Wl, j * Wl, Wl, Wl))

	pygame.display.update()