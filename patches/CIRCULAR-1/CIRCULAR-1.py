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
    
    x0 = 960#random.randrange(0,1920)
    x1 = 960 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
   # y = i * 10#random.randrange(0,1080)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    R = mvp.knob2
    R = R + (mvp.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, color, [620, 360], [x, y], mvp.knob1 / 50)
    
    #pygame.draw.line(screen, color, [x0 , y ], [x1 , y+10], 10)

