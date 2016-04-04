import os
import pygame
import time
import random

note_down = False

def setup(screen, mvp):
    pass

def draw(screen, mvp):
    #screen.fill( (0, 0, 0))
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i):
    
    x0 = 540#random.randrange(0,1920)
    x1 = 540 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 19#random.randrange(0,1080)
    #bw = random.randrange(0,255)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    
    pygame.draw.circle(screen,color,(y, x1),8, 0)
    pygame.draw.line(screen, color, [y, x0], [y, x1], 2)

