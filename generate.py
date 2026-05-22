from random import shuffle
import pygame

# settings
W, H = 20, 20
Tile = 25
FPS = 1000

#generate map

text_map = []
for i in range(W * 2 + 1):
	text_map.append([])
	for j in range(H * 2 + 1):
		if ((j % 2 == 0) or (i % 2 == 0)) or ((i == 0) or (j == 0)):
			text_map[i].append('1')
		else:
			text_map[i].append('.')

def generate():
	for i in range(len(cells)):
		for j in range(len(cells[i])):
			text_map[i * 2 + 1][j * 2 + 1] = '.'
			if not cells[i][j].walls['up']:
				text_map[i * 2 + 1][j * 2] = '.'
			if not cells[i][j].walls['down']:
				text_map[i * 2 + 1][j * 2 + 2] = '.'
			if not cells[i][j].walls['right']:
				text_map[i * 2 + 2][j * 2 + 1] = '.'
			if not cells[i][j].walls['left']:
				text_map[i * 2][j * 2 + 1] = '.'

def save():
	f = open("levels/1.txt", "w+")
	save_text = str(W * 2 + 1) + '\n'
	for i in range(len(text_map)):
		for j in range(len(text_map[i])):
			save_text += text_map[i][j]
		#save_text += '1'
		save_text += '\n'

	# for i in range(len(text_map[0]) + 1):
	# 	save_text += '1'

	f.write(save_text)
	f.close()

# update func
def update(x, y):
	h = [[-1, 0], [1, 0], [0, 1], [0, -1]]
	res = []
	for i in h:
		if (x + i[0] >= 0 and x + i[0] < W) and (y + i[1] >= 0 and y + i[1] < H):
			res.append(i)
	result = []
	for i in res:
		if not cells[x + i[0]][y + i[1]].visited:
			result.append(i)

	if len(result) == 0:
		return False
	else:
		shuffle(result)
		return result[0]

# cell class
class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.visited = False
		self.walls = {'up' : True, 'right' : True, 'down' : True, 'left' : True}

	def draw_r(self, sc):
		pygame.draw.rect(sc, (0, 60, 0), (self.x * Tile, self.y * Tile, Tile, Tile))

	def draw(self, sc):
		if self.visited:
			self.color = (0, 120, 0)
		else:
			self.color = (60, 60, 60)
		if self in stack:
			self.color = (120, 0, 0)
		pygame.draw.rect(sc, self.color, (self.x * Tile, self.y * Tile, Tile, Tile))
	def draw_w(self, sc):
		if self.walls['up']:
			pygame.draw.line(sc, (255, 255, 255), (self.x*Tile, self.y*Tile), (self.x*Tile + Tile, self.y*Tile))
		if self.walls['down']:
			pygame.draw.line(sc, (255, 255, 255), (self.x*Tile, self.y*Tile + Tile), (self.x*Tile + Tile, self.y*Tile + Tile))
		if self.walls['left']:
			pygame.draw.line(sc, (255, 255, 255), (self.x*Tile, self.y*Tile), (self.x*Tile, self.y*Tile + Tile))
		if self.walls['right']:
			pygame.draw.line(sc, (255, 255, 255), (self.x*Tile + Tile, self.y*Tile), (self.x*Tile + Tile, self.y*Tile + Tile))

# programm
pygame.init()

clock = pygame.time.Clock()

sc = pygame.display.set_mode((W*Tile + 1, H*Tile + 1))

cells = []
for i in range(W):
	cells.append([])
	for j in range(H):
		cells[i].append(Cell(i, j))

cell_r = cells[0][0]
stack = []

# main loop
while True:
	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			exit()
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_ESCAPE:
				exit()
	sc.fill((0, 0, 0))

	cell = update(cell_r.x, cell_r.y)
	if cell != False:
		cell_start = cell_r
		cell_stop = cells[cell_r.x + cell[0]][cell_r.y + cell[1]]

		if cell[0] == 1:
			cell_start.walls['right'] = False
			cell_stop.walls['left'] = False

		if cell[0] == -1:
			cell_start.walls['left'] = False
			cell_stop.walls['right'] = False

		if cell[1] == 1:
			cell_start.walls['down'] = False
			cell_stop.walls['up'] = False

		if cell[1] == -1:
			cell_start.walls['up'] = False
			cell_stop.walls['down'] = False
		cell_start.visited = True
		stack.append(cell_start)
		cell_r = cell_stop
	else:
		cell_r.visited = True
		if len(stack) != 0:
			cell_r = stack[len(stack) - 1]
			stack.pop()
		else:
			generate()
			save()
			break

	for i in range(W):
		for j in range(H):
			if (cells[i][j] in stack) or (cells[i][j].visited):
				cells[i][j].draw(sc)

	for i in range(W):
		for j in range(H):
			if (cells[i][j] in stack) or (cells[i][j].visited):
				cells[i][j].draw_w(sc)			

	cell_r.draw_r(sc)
	cell_r.draw_w(sc)

	pygame.display.update()

	clock.tick(FPS)