from settings import *
from random import randint
from settings import *
from enemy import Enemy

import pygame
import os

text_map = []
temp_map = []
levels = []

levels_2 = os.listdir("levels")
for i in levels_2:
	temp_map = []
	f = open("levels/" + i, "r")
	for i in range(int(f.readline())):
		temp_map.append(f.readline())
	levels.append(temp_map)

colors = {}
world_map = {}
world_map2 = set()
world_map3 = set()
level = 0
levels_done = set()

def set_lvl(lvl):
	global level
	world_map = {}
	if lvl < len(levels):
		level = lvl

def next_lvl(player):
	global level
	world_map = {}
	player.x = 150
	player.y = 150

	if (len(levels_done) != len(levels)):
		levels_done.add(level)
		level = max(levels_done) + 1
	if (len(levels_done) == len(levels)):
		exit()

def update_map(player):
	global world_map, world_map2, world_map3
	text_map = levels[level]
	colors = {}
	world_map2.clear()
	world_map3.clear()

	for j, row in enumerate(text_map):
		for i, char in enumerate(row):
			if char != '.':
				if char == '1':
					world_map[(i * TITLE, j * TITLE)] = '1'
				elif char == '2':
					world_map[(i * TITLE, j * TITLE)] = '2'
			if char == 'O':
				world_map2.add((i * TITLE, j * TITLE))
				colors[(i * TITLE, j * TITLE)] = '2'
			if char == 'P':
				world_map3.add((i * TITLE, j * TITLE))
				colors[(i * TITLE, j * TITLE)] = '1'
colors[(100, 0)] = '2'