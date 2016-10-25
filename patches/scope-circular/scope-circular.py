import os
import pygame
import time
import random
import math

note_down = False

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 960
    x1 = 960 + (mvp.audio_in[i] / 35)
   
    color = mvp.color_picker()
    R = int(mvp.knob2*1000)
    R = R + (mvp.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, color, [620, 360], [x, y], int(mvp.knob1*20))
    

