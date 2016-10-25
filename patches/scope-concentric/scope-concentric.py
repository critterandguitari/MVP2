import os
import pygame
import time
import random

size = 400
count = 0

def setup(screen, mvp):
    pass

def draw(screen, mvp):
    global size, count


    
    if True: #mvp.note_on :
        
        count += 1
        if count > 7 :
            count = 0
            screen.fill((0,0,0))
        for x in range(0, 10):
            size -= 2
            if size < 2:
                size = 400
            x = screen.get_rect().centerx
            y = screen.get_rect().centery
    #size = mvp.knob2
    
    # force c1 into 0 - 255  (otherwise error, i think)
            c1 = int(size * int(mvp.knob2 * 100)) & 0xff 
            color = (c1, 255 - c1, c1)
            pygame.draw.circle(screen,color,[x,y],size)
    #time.sleep(.1)


    
        
