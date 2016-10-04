import os
import pygame
import time
import random
import pygame.gfxdraw

count = 0

def setup(screen, mvp):
    print "setting up random pies ..."

def draw(screen, mvp):
    
    global count
    if mvp.note_on:
        
        count += 1  
        if count > mvp.knob3:
            count = 0
            screen.fill((0,0,0))
        
        #if count > mvp.knob3 //
        x=random.randrange(0,700)
        y=random.randrange(0,400)
        pierad=random.randrange(10,100) #radius
        arcstart=random.randrange(0,360)
        arcend=random.randrange(0, 360-arcstart)
        size = mvp.knob2
        #color = (random.randrange(254,255), random.randrange(100,255), random.randrange(0,255))
        
        #color = pygame.Color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), (float(mvp.knob4) / 1024) * 100)
        coloralpha=mvp.knob4/4
#        size = mvp.knob2
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), coloralpha)
        #color.hsva = ((float(mvp.knob4) / 1024) * 360, 100, 100, (float(mvp.knob4) / 1024) * 100)
        
        
        fillrange=mvp.knob1/10
        for i in range(fillrange):
            pygame.gfxdraw.pie(screen, x, y, size, arcstart + i*2, arcend - i*2, color)
        
#		pygame.gfxdraw.pie(screen, x, y, pierad, 5, 50, color)
#        pygame.draw.circle(screen,color,[x,y],size, 0)
#        pygame.gfxdraw.aacircle(screen, x, y, size, color)
#        pygame.gfxdraw.filled_circle(screen, x, y, size, color)

#pgyame.gfxdraw.pie(surface, x, y, radius, arcstart, arcend, color): return None
