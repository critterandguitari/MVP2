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
    
    x0 = 640
    x1 = 640 + (mvp.audio_in[i] / 35)
    y = i * 7
    color = mvp.color_picker()
    
    pygame.draw.line(screen, color, [x0 + 0 + int(mvp.knob1*1000), y + i], [x1 + 0 + int(mvp.knob2 *1000), y+10], 10)
    

