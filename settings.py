import math

# game settings
WIDTH = 1200
HEIGHT = 600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TITLE = 100
COLLUM = 10

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 240
MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TITLE
SCALE = WIDTH // NUM_RAYS

# texture settings
TEXTURE_WIDTH = 256
TEXTURE_HEIGHT = 256
TEXTURE_SCALE = TEXTURE_HEIGHT // TITLE

# sprite settings
DUBBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1

# player settings
player_pos = 150, 150
player_angle = 0
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 220)
DARKGRAY = (110, 110, 110)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)