import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    for i in range(0, 25) :
        seg(screen, mvp, i * 4)    

def seg(screen, mvp, i) :
    
    x0 = 640#random.randrange(0,1920)
    x1 = 640 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 10#random.randrange(0,1080)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    
    pygame.draw.line(screen, color, [x0 + i * mvp.knob1, y], [x1 + i, y], 40)
    #pygame.draw.line(screen, color, [x0 , y ], [x1 , y+10], 10)

