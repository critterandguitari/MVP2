import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

note_down = True



def draw(screen, mvp):
    
    global note_down

    if mvp.note_on :
        note_down = True
        print note_down
    if mvp.note_off :
        note_down = False
        print note_down

    if True :
        x=(random.randrange(0,1300) - 100)
        y=(random.randrange(0,750) - 100)
        y1=random.randrange(0,750)
        x1=random.randrange(0,1300)
        #use values below if you want traps 'centered'
        #x=(random.randrange(0,640)-100)
        #y=(random.randrange(0,360)-100)
        #y1=random.randrange(360,800)
        #x1=random.randrange(656,1300)
        size = random.randrange(0,200)
        width = int(mvp.knob2 * 1000) 
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        pygame.draw.line(screen, color, [x, y], [x1, y1], width)


