import pygame as pg
import sys
from os import path
from Settings import *
from Sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        #initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 10 ,10)
        for x in range(10, 10):
            Wall(self, x, 5)

    def run(self):
        #Game Loop - set self.playing = False to end the game
        self.playing = True
        while self.playing == True:
            self.dt = self.clock.tick(FPS) / 1000
            self.events() # physics and logic
            self.update() # Updates current state of the Game
            self.draw() # Visualizes Update() for the player by drawing it on the screen

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        #updates a portion of the game Loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        #self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        #catch all events here like inputs and stuff
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_u:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

#create game Loop
g = Game()
while True:
    g.new()
    g.run()
