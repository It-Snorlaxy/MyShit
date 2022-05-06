# Pygame template - skeleton for new games made by KidsCanCode

import pygame
import random

width = 360
height = 480
fps = 30

# Define colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(fps)
    # v There are 3 componets of a game loop v
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Draw/Render/Display
    screen.fill(Black)
    # *after* drawing everything, flip the display -Double Buffering-
    pygame.display.flip()

pygame.quit()
