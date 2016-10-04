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
    
    x = 960 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 10#random.randrange(0,1080)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    
    pygame.draw.line(screen, color, [x, y], [x, y+10], 10)

