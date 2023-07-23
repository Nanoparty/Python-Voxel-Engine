#from numba import njit
import numpy as np
import glm
import math

# OpenGL settings
NUM_SAMPLES = 16 # antialiasing

# resolution
WIN_RES = glm.vec2(1280, 720)

# world generation
SEED = 16

# ray casting
MAX_RAY_DIST = 6

# chunk
CHUNK_SIZE = 48
H_CHUNK_SIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE
CHUNK_SPHERE_RADIUS = H_CHUNK_SIZE * math.sqrt(3)

# world
WORLD_W, WORLD_H = 20, 2
WORLD_D = WORLD_W
WORLD_AREA = WORLD_W * WORLD_D
WORLD_VOL = WORLD_AREA * WORLD_H

# world center
CENTER_XZ = WORLD_W * H_CHUNK_SIZE
CENTER_Y = WORLD_H * H_CHUNK_SIZE

# camera
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG) # vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO) # horizontal fov
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# player
PLAYER_SPEED = 0.015
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(CENTER_XZ, WORLD_H * CHUNK_SIZE, CENTER_XZ)
MOUSE_SENSITIVITY = 0.002

# colors
BG_COLOR = glm.vec3(0.58, 0.83, 0.99)

# textures
VOID = 0
SAND = 1
GRASS = 2
DIRT = 3
STONE = 4
SNOWY_GRASS = 5
LEAVES = 6
OAK_WOOD = 7
WATER = 8
GLASS = 9
OAK_PLANK = 10
GRAVEL = 11
COAL_ORE = 12
IRON_ORE = 13
GOLD_ORE = 14
LAPIS_ORE = 15
REDSTONE_ORE = 16
DIAMOND_ORE = 17
EMERALD_ORE = 18
ICE = 19
BRICK = 20
COBBLESTONE = 21
BEDROCK = 22
SANDSTONE = 23
SMOOTHSTONE = 24
STONE_BRICKS = 25
PUMPKIN = 26
TNT = 27
FURNACE = 28
BOOKSHELF = 29
CRAFTING_TABLE = 30
SPONGE = 31
PRISMARINE_LAMP = 32
GLOWSTONE = 33
IRON_BLOCK = 34
GOLD_BLOCK = 35
REDSTONE_BLOCK = 36
DIAMOND_BLOCK = 37
EMERALD_BLOCK = 38
MOSSY_COBBLESTONE = 39
MELON = 40
HAY = 41
LAPIS_BLOCK = 42
BIRCH_WOOD = 43
BIRTH_PLANKS = 44
RED_TULIP = 45
WHITE_TULIP = 46
PINK_TULIP = 47
PEONY = 48
ORANGE_TULIP = 49
RED_MUSHROOM = 50
DANDELION = 51
LILLY_PAD = 52
SHORT_GRASS = 53
TALL_GRASS = 54

NUM_BLOCKS = 54
TRANSPARENT_BLOCKS_SINGLE = [WATER, GRASS]
TRANSPARENT_BLOCKS = [LEAVES, RED_TULIP, WHITE_TULIP, PINK_TULIP, ORANGE_TULIP, PEONY, LILLY_PAD, RED_MUSHROOM, SHORT_GRASS, TALL_GRASS]

# terrain levels
SNOW_LVL = 54
STONE_LVL = 49
DIRT_LVL = 40
GRASS_LVL = 8
SAND_LVL = 7
WATER_LVL = 5

# tree settings
TREE_PROBABILITY = 0.02
TREE_WIDTH, TREE_HEIGHT = 4, 8
TREE_H_WIDTH, TREE_H_HEIGHT = TREE_WIDTH // 2, TREE_HEIGHT // 2

# terrain objects
PUMPKIN_PROBABILITY = 0.002
FLOWER_PROBABILITY = 0.05
MUSHROOM_PROBABILITY = 0.01
SHRUB_PROBABILITY = 0.3
