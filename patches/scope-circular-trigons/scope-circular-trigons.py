import os
import pygame
import time
import random
import math
import pygame.gfxdraw

def setup(screen, mvp):
    pass

note_down = False
lx = 0
ly = 0

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    global lx, ly
    x0 = 960#random.randrange(0,1920)
    x1 = 960 + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
   # y = i * 10#random.randrange(0,1080)
    #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    color = mvp.color_picker()
    R = int(mvp.knob1 * 1000)
    R = R + (mvp.audio_in[i] / 100)
    x = R * math.cos((i /  100.) * 6.28) + 640
    y = R * math.sin((i /  100.) * 6.28) + 260
    
    #pygame.draw.line(screen, color, [lx, ly], [x, y], 1)
    #pygame.draw.circle(screen,color,[int(x), int(y)], mvp.knob1 / 50, 0)
    if ((i % 2)) :
        pygame.gfxdraw.filled_trigon(screen, int(x), int(y), int(x) + int(mvp.knob2*200) + random.randrange(0,78), int(y) + int(mvp.knob2*200), int(x) - int(mvp.knob3*200), int(y) + int(mvp.knob3*200), color)
    else :
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        pygame.gfxdraw.trigon(screen, int(x), int(y), int(x) + int(mvp.knob2*200) + random.randrange(0,78), int(y) + int(mvp.knob2*200), int(x) - int(mvp.knob3*200), int(y) + int(mvp.knob3*200), color)

    
    #pygame.draw.line(screen, color, [x0 , y ], [x1 , y+10], 10)

