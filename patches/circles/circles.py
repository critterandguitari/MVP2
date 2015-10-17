import os
import pygame
import time
import random
import pygame.gfxdraw

def setup(screen, mvp):
    print "setting up random circles ..."

def draw(screen, mvp):
    if mvp.quarter_note :
        #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        color = (random.randrange(0,25), random.randrange(0,25), random.randrange(0,25))
        screen.fill(color) 
          

    if True:#mvp.note_on :
        x=random.randrange(0,1920)  + mvp.knob2 // 2
        y=random.randrange(0,1080)  + mvp.knob3 // 2
        size = mvp.knob1 // 20 + 20
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0, 255))
        #color = pygame.Color.hsva( (float(mvp.knob3) / 1024) * 360, 100, 100, 50)#(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        #color = Color.hsva( 20, 100, 100, 50)#(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = mvp.knob1 // 50
        if width == 0 : width = 1
        if width > size : width = size
        pos = (x,y)#pygame.mouse.get_pos()
        pygame.draw.circle(screen,color,pos,size, 0)
        pygame.gfxdraw.aacircle(screen, x, y, size, color)
        #pygame.gfxdraw.filled_circle(screen, x, y, size, color)
