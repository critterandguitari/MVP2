import os
import pygame
import time
import random

count = 0

TRANSPARENT = (255,255,255)
bg = pygame.Surface((1920,1080))
mask = pygame.Surface((1920,1080))
mask.set_colorkey(TRANSPARENT)
mask.fill((0,0,0))

def inc() :
    global count
    count += 1


def draw(screen, mvp):
    
    global bg, mask, count
    
    if mvp.note_on :
        count += 1
        if count > (mvp.knob3 // 10)  : count = 0

        if count == 0:
            #mask.fill((random.randrange(0,255), random.randrange(0,255), random.randrange(0,255)))
            mask.fill((19,23,9))

    # 
        x=random.randrange(0,1920)
        y=random.randrange(0,1080)
        y1=random.randrange(0,1080)
        x1=random.randrange(0,1920)
        size = random.randrange(0,200)
        width = mvp.knob2#random.randrange(100,255)
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        pygame.draw.line(bg, color, [x, y], [x1, y1], width)
        rect = bg.get_rect()
        screen.blit(bg, rect)
    
        x=random.randrange(0,1920)  
        y=random.randrange(0,1080)  
        size = mvp.knob1
        pos = (x,y)
        pygame.draw.circle(mask,TRANSPARENT,pos,size, 0)
        rect = mask.get_rect()
    
    
        screen.blit(mask, rect)
    
   #time.sleep(.25)


