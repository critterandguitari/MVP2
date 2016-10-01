import os
#import pygame_sdl2
#pygame_sdl2.import_as_pygame()
import pygame
import time
import random

from pygame.locals import *
pygame.init()


print "opening frame buffer"
#screen = fullfb.init()
screen = pygame.display.set_mode((500,500),  pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE  )

while 1:

    # quit on esc
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255))) 

    pygame.display.flip()
    

time.sleep(1)


print "Quit"
