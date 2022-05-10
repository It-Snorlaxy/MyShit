import pygame as pg
from os import path

#definere some colors (R,G,B)
TRANSPARENT = (0, 0, 0, 0) #Den fjered værdi er opacity (R,G,B,opacity)
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
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
