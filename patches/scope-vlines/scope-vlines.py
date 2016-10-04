import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 960#random.randrange(0,1920)
    x1 = 960 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    y = i * 10#random.randrange(0,1080)
    color = mvp.color_picker()
    
    pygame.draw.line(screen, color, [x0, y], [x1, y], 10)

