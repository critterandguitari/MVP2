import os
import pygame
import time
import random
import math

note_down = False
lx = 0
ly = 0

def draw(screen, mvp):
    screen.fill( (0, 0, 0))
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    global lx, ly
    x0 = 960#random.randrange(0,1920)
    x1 = 960 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
   # y = i * 10#random.randrange(0,1080)
    color = (random.randrange(0,255))#, random.randrange(0,255), random.randrange(0,255))
    color = (color, color, color)
    R = mvp.knob2
    R = R + (mvp.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 360
    
    pygame.draw.line(screen, color, [lx, ly], [x, y], 1)
    ly = y
    lx = x
    pygame.draw.circle(screen,color,[int(x), int(y)], mvp.knob1 / 50, 0)

    
    #pygame.draw.line(screen, color, [x0 , y ], [x1 , y+10], 10)

