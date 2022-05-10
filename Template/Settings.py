import pygame as pg
import sys
from os import path
pg.init()

#define some colors (R,G,B)
TRANSPARENT = (0, 0, 0, 0) #Den fjered værdi er opacity (R,G,B,opacity)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW =(255, 255, 0)


WIDTH = 1024 #Easy Division '/' = 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768 #Easy Division '/' = 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = 'TEMPLATE'
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE



#Folder structure
game_folder = path.dirname(__file__)
assets_folder = path.join(game_folder, 'assets')
map_folder = path.join(game_folder, 'Maps')

pg.display.set_mode((WIDTH, HEIGHT))

#assets
PLAYER_ASSET = pg.image.load(path.join(assets_folder, 'player.png')).convert_alpha()
ENEMY_ASSET = pg.image.load(path.join(assets_folder, 'Enemy.png')).convert_alpha()
