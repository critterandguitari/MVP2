import os
import pygame
import time
import random
import pygame.gfxdraw

count = 0
ranx = 0
rany = 0

def setup(screen, mvp):
    print "setting up random circles ..."

def draw(screen, mvp):
    global count, rany, ranx
    
    if True: #mvp.note_on :
        
        count += 1  
        if count > mvp.knob3 // 20:
            count = 0
            #screen.fill((0,0,0))
            rany = random.randrange(0,screen.get_height())#random.randomrange(0, screen.get_height())
            ranx = random.randrange(0,screen.get_width())#random.randomrange(0, screen.get_width())

        x=ranx + count * 4
        y=rany + count * 4
        size = 20 + count
        color = (random.randrange(0,250), random.randrange(0,250), random.randrange(0,255))

        pos = (x,y)#pygame.mouse.get_pos()
        pygame.draw.circle(screen,color,pos,size, 0)
        time.sleep(.05)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
#        pygame.gfxdraw.filled_circle(screen, x, y, size, color)
