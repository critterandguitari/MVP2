import os
import pygame
import time
import random
import pygame.gfxdraw

count = 0

def draw(screen, mvp):

    global count 
    
    
    
    if mvp.note_on :
        do16(screen)
        do16(screen)
        do16(screen)
        do16(screen)

def do16(screen) :
    doit(screen)
    doit(screen)
    doit(screen)
    doit(screen)

    doit(screen)
    doit(screen)
    doit(screen)
    doit(screen)

    doit(screen)
    doit(screen)
    doit(screen)
    doit(screen)

    doit(screen)
    doit(screen)
    doit(screen)
    doit(screen)



def doit (screen) :
    x=random.randrange(0,1920)
    y=random.randrange(0,1080)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    size = 10
    pos = (x,y)
#        pygame.draw.circle(screen,color,pos,size, 0)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
    pygame.gfxdraw.filled_circle(screen, x, y, size, color)

   
