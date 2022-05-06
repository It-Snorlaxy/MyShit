# pygame template - skeleton for new games made by KidsCanCode

import pygame as pg
import random
#from sprites import *

WIDTH = 360
HEIGHT = 480
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pg.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        #Needed for every sprite
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("player.png")
        self.rect = self.image.get.rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

#initialize pygame and create window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    # v There are 3 componets of a game loop v
    # Process input (events)
    for event in pg.event.get():
        # check for closing the window
        if event.type == pg.QUIT:
            running = False
    # Update
    all_sprites.update()

    # Draw/Render/Display
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display -Double Buffering-
    pg.display.flip()

pg.quit()
