import os
import pygame
import time
import random
import pygame.gfxdraw

note_down = False

def draw(screen, mvp):

    for i in range(0, 100) :
        square(screen)  

def square(screen):
    x = random.randrange(0,screen.get_width())
    y = random.randrange(0,screen.get_height())
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    #pygame.draw.line(screen, color, [x, y], [x,y+100 ], 100)
    #pygame.draw.rect(screen, color, [x, y, x+100,y+100 ], 10)
    pygame.gfxdraw.box(screen, [x, y, x+100,y+100 ], color)
