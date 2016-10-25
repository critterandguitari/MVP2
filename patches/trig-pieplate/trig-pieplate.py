import os
import pygame
import time
import random
import pygame.gfxdraw

count = 0

def setup(screen, mvp):
    pass

def draw(screen, mvp):
    
    global count
    if True: #mvp.note_on:
        
        
        #if count > mvp.knob3 //
        x=random.randrange(0,1300)
        y=random.randrange(0,800)
        pierad=random.randrange(10,100) #radius
        arcstart=random.randrange(0,360)
        arcend=random.randrange(0, 360-arcstart)
        size = int(mvp.knob2 * 1000)
        color = mvp.color_picker()
        

        fillrange=int(mvp.knob1*100)
        for i in range(fillrange):
            pygame.gfxdraw.pie(screen, x, y, size, arcstart + i*2, arcend - i*2, color)

