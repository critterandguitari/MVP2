import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 640#random.randrange(0,1920)
    x1 = 640 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 8#random.randrange(0,1080)
    bw = random.randrange(0,255)
    color = (bw, bw, bw)
    
    pygame.draw.circle(screen,color,(x1, y),100, 0)
    pygame.draw.line(screen, color, [x0, y], [x1, y], 2)

