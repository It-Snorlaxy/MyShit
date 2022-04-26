# import the pygame module, so you can use it
import pygame
import keyboard

class main:
    # define a main function
    def main():

        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load("player.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Tutorial")

        # create a surface on screen that has the size of 240 x 180
        screen = pygame.display.set_mode((1000,1000))
        # define a variable to control the main loop
        running = True
        pygame.image.get_extended()
        image = pygame.image.load("player.png")
        screen.fill((69,69,69))
        screen.blit(image, (500,500))
        pygame.display.flip()

        screen_width = 1000
        screen_height = 1000
        xpos = 25
        ypos = 25
        step_x = 0.8
        step_y = 0.8
    # how many pixels we move our smiley each frame

            # main loop
        while running:
            if xpos > screen_width-40:
                xpos = screen_width-40
            if xpos<0:
                xpos = 0
            if ypos>screen_height-40:
                ypos = screen_height-40
            if ypos<0:
                ypos = 0

        # update the position of the smiley
            if keyboard.is_pressed('d'):
                xpos += step_x # move it to the right
            if keyboard.is_pressed('s'):
                ypos += step_y # move it down
            if keyboard.is_pressed('a'):
                xpos += -step_x # move it to the right
            if keyboard.is_pressed('w'):
                ypos += -step_y # move it to the right

            screen.fill((69,69,69))
            screen.blit(image, (xpos, ypos))
            pygame.display.flip()
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

class Grid:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = {}

        for x in range(width):
            for y in range(height):
                self.cells[(x,y)]=Cell()

class Cells:

    def type():
        pass

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
