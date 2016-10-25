import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

note_down = False

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 360
    x1 = 360 + (mvp.audio_in[i] / 35)
    y = i * 11
    bw = random.randrange(0,255)
    color = (bw, bw, bw)
    
    pygame.draw.circle(screen,color,(y, x1),5, 0)
    pygame.draw.line(screen, color, [y, x0], [x1, y], 2)

