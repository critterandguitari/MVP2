import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 640
    x1 = 640 + (mvp.audio_in[i] / 35)
    y = i * 10
    color = mvp.color_picker()
    
    pygame.draw.line(screen, color, [x0, y], [x1, y], 10)

