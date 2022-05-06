import pygame
import random
from main import *

player = Player()

class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        #Needed for every sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get.rect()
        self.rect.center = (width / 2, height / 2)
