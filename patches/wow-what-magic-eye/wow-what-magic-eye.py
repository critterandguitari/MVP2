import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    screen.fill( (0, 0, 0))
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 540#random.randrange(0,1920)
    x1 = 540 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 11#random.randrange(0,1080)
    bw = random.randrange(0,255)
    color = (bw, bw, bw)
    
    pygame.draw.circle(screen,color,(y, x1),5, 0)
    pygame.draw.line(screen, color, [y, x0], [x1, y], 2)

