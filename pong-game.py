from ball import Ball
from paddle import Paddle
import pygame
import random
 
def main():
     
    # initialize the pygame module
    pygame.init()
    
    # SCREEN 
    pygame.display.set_caption("Pauls Pong")    # WINDOW TITLE
    screen = pygame.display.set_mode((750,500)) # SIZE

    # BACKROUND
    bgColor = (160, 165, 173)
    screen.fill(bgColor)

    #VARIABLES
    FPS = 240
    clock = pygame.time.Clock()
    xVelocity = random.randint(1,6)
    yVelocity = random.randint(-3,3)


    topL = (0,0) 
    topR = (750,0)
    bottomL = (0,500)
    bottomR = (750,500)

    # WALLS
    wColor = (45, 47,51)
    pygame.draw.line(screen, wColor, topL, bottomL, 50)    # LEFT WALL
    pygame.draw.line(screen, wColor, topL, topR, 50)       # TOP WALL
    pygame.draw.line(screen, wColor, bottomL, bottomR, 50) # BOTTOM WALL
    pygame.display.flip()

    # BALLS
    x1 = (750-Ball.radius)
    y1 = (250)
    xv1 = (-(random.randint(1,5)))
    yv1 = (random.randint(-3,3))
    b1 = Ball(x1,y1, xv1,yv1, screen, wColor, bgColor)
    b1.show(wColor)
     
    x2 = (750-Ball.radius)
    y2 = (250)
    xv2 = (-(random.randint(1,5)))
    yv2 = (random.randint(-3,3))
    b2 = Ball(x2,y2, xv2,yv2, screen, wColor, bgColor)
    b2.show(wColor)

    
    pygame.display.flip()

    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.flip()    
        clock.tick(FPS) 
        b1.update()
        b2.update()

    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()