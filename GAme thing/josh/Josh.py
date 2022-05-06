# import the pygame module, so you can use it and keyboard to check for input
import pygame
import keyboard
import random
import time

# initialize the pygame module
pygame.init()

transparent = (0, 0, 0, 0) #Laver en RGB variabel med "farven" gennemsigtig
#Bestemmer skærmens højde og bredde
screen_width = 1000
screen_height = 1000
#Laver en textfont som bruges til at vise tekst på skærmen
Text = pygame.font.SysFont(None, 32)
#Pixel positionen til brug til at placere teksten
textH = 500
textW = 400

#Define a main function
def main():
    #Pygame skal bruge en defineret screen som spillet vises på
    screen = pygame.display.set_mode((screen_width, screen_height))
    #Allows us to open png
    pygame.image.get_extended()
    #load and set the logo
    logo = pygame.image.load("player.png")
    pygame.display.set_icon(logo)
    #Gives a title
    pygame.display.set_caption("Fighting Engine")
    #Starts the pygame
    running = True
    #Then we load and display the player and an enemy, right after filling the screen in colour
    image = pygame.image.load("player.png")
    enemiage = pygame.image.load("enemy.png")
    screen.fill((109, 136, 157))
    screen.blit(image, (250, 250))
    screen.blit(enemiage, (500, 500))
    pygame.display.flip()

    #Defines the parameters of movement for player
    xpos = 25
    ypos = 25
    step_x = 0.8
    step_y = 0.8

        # main loop
    while running:
        #This essentially stops player movement so they don't run of screen
        if xpos > screen_width - 40:
            xpos = screen_width - 40
        if xpos < 0:
            xpos = 0
        if ypos > screen_height - 40:
            ypos = screen_height - 40
        if ypos < 0:
            ypos = 0

        #Starts combat if the player enters these coordinats, to test the combat system
        if 500 <= xpos <= 550 and 500 <= ypos <= 550:
            combat()


    # Update the position of the smiley
        if keyboard.is_pressed('d') or keyboard.is_pressed('right arrow'):
            xpos += step_x # move it to the right
        if keyboard.is_pressed('s') or keyboard.is_pressed('down arrow'):
            ypos += step_y # move it down
        if keyboard.is_pressed('a') or keyboard.is_pressed('left arrow'):
            xpos += -step_x # move it to the left
        if keyboard.is_pressed('w') or keyboard.is_pressed('up arrow'):
            ypos += -step_y # move it up
        #Her er lavet en måde at stoppe spillet undervejs på
        if keyboard.is_pressed('esc'):
            running = False
        #To update the screen so you know what happens, we fill the screen, then put in the player in its correct position and the enemy
        screen.fill((109, 136, 157))
        screen.blit(image, (xpos, ypos))
        screen.blit(enemiage, (500, 500))
        pygame.display.flip()
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

#Makes a new screen specifically for combat
cscreen = pygame.display.set_mode((screen_width, screen_height))


def combat():
    #A list of enemies to randomly be chosen when combat is called
    enemies = ["Atom", "Birb", "Python"]
    enemy = random.choice(enemies)
    #Depending on which enemy it is, health is defined to fit
    if enemy == "Atom":
        enemyHP = 120
    elif enemy == "Birb":
        enemyHP = 80
    elif enemy == "Python":
        enemyHP = 160
    #Shows on screen which enemy you're going to face
    appear = Text.render(("A wild " + enemy + " appeared"), True, pygame.Color('white'))
    cscreen.blit(appear, (textW, textH))
    pygame.display.flip()
    #After 2 seconds we "reset" the screen
    time.sleep(2)
    cscreen.fill(transparent)
    pygame.display.flip()
    #Starts combat running loop
    crunning = True
    #Makes enemy health
    currentEHP = enemyHP
    time.sleep(0.5)
    while crunning == True:
        if keyboard.is_pressed('esc'):
            crunning = False
        #fimage = pygame.image.load("combat-zone.png")
        enemypicture = pygame.image.load("enemy.png")#enemy + ".png")
        #cscreen.blit(fimage, (screen_width - 220, screen_height - 410))
        cscreen.blit(enemypicture, (screen_width - 1000, screen_height - 1000))
        pygame.display.flip()
        currentEHP, DMGModifier = playerAttack(currentEHP)
        if currentEHP > 0:
            enemyAttack(enemy)
        else:
            cscreen.fill(transparent)
            Vic = Text.render(("You have won! Congratulations!"), True, pygame.Color('gold'))
            cscreen.blit(Vic, (textW, textH))
            pygame.display.flip()
            time.sleep(2)
            crunning = False

    #enemyAttack(enemy)
def playerAttack(currentEHP):
    print('playerAttack')
    playerDMG = 0
    enemyDMG = 0
    enemyHP = currentEHP
    while True:
        if keyboard.is_pressed('esc'):
            crunning = False
        moveChoice = Text.render(("Choose your move (1, 2, 3, 4)"), True, pygame.Color('white'))
        ehp = Text.render((str(enemyHP)), True, pygame.Color('white'))
        cscreen.blit(ehp, (textW, 100))
        cscreen.blit(moveChoice, (textW, textH))
        pygame.display.flip()
        cscreen.fill(transparent)
        enemypicture = pygame.image.load("enemy.png")
        cscreen.blit(enemypicture,(screen_width - 1000, screen_height - 1000))
        if keyboard.is_pressed("1"):
            playerMove = Text.render(("You punched"), True, pygame.Color('white'))
            playerDMG = 30
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True, pygame.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pygame.display.flip()
            time.sleep(1)
            return enemyHP, 1
        elif keyboard.is_pressed("2"):
            playerMove = Text.render(("You kicked"), True, pygame.Color('white'))
            playerDMG = 40
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True , pygame.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pygame.display.flip()
            time.sleep(1)
            return enemyHP, 1
        elif keyboard.is_pressed("3"):
            playerMove = Text.render(("You screamed"), True, pygame.Color('white'))
            dmgreductext = Text.render(("Enemy will do 10% less dmg next attack"), True, pygame.Color('white'))
            playerDMG = 15
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True, pygame.Color('white'))
            dmgreduc = 0.9
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            cscreen.blit(dmgreductext, (textW, textH + 100))
            pygame.display.flip()
            time.sleep(1)
            return enemyHP, dmgreduc
        elif keyboard.is_pressed("4"):
            playerMove = Text.render(("You defended yourself"), True, pygame.Color('white'))
            dmgtext = Text.render(("You take 90% less dmg"), True, pygame.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pygame.display.flip()
            dmgreduc = 0.1
            time.sleep(1)
            crunning = False
            return enemyHP, dmgreduc
#def dmgcalculation:

def enemyAttack(enemy):
    if enemy == "Atom":
        moves = [2,3,4]
        move = random.choice(moves)
    elif enemy == "Birb":
        moves = [1,5]
        move = random.choice(moves)
    elif enemy == "Python":
        moves = [2,3,4]
        move = random.choice(moves)

    if move == 1:
        emove = Text.render((enemy + " used kick!"), True, pygame.Color('white'))
        edmg = Text.render(('It dealt 20 dmg'), True, pygame.Color('red'))
        enemyDMG = 20
        cscreen.blit(emove, (textW, textH))
        cscreen.blit(edmg, (textW, textH + 50))
        pygame.display.flip()
        time.sleep(2)
        return enemyDMG
    elif move == 2:
        print(enemy + " used bug!")
        print("Does critical dmg")
        print('Took 40 dmg')
    elif move == 3:
        print(enemy + " crashed")
        print("You won the battle")
    elif move == 4:
        print(enemy + " used error")
        print("does 45 dmg")
    elif move == 5:
        print(enemy + " used schreech")
        print("You take 5 dmg")
        #print("You do 10% less dmg next attack")

# run the main function only if this module is executed as the main scripts
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    #combat()
