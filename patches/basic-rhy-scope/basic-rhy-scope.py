import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

def draw(screen, mvp):
    above = False
    for i in range(0, 100) :
        if abs(mvp.audio_in[i]) > 2000 :
            above = True
    
    if above :
        #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        #screen.fill(color)

        size = 64
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0, 255))
        pos = (random.randrange(0,1920),random.randrange(0,1080))
        pygame.draw.circle(screen,color,pos,size, 0)


