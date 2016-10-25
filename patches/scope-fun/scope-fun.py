import os
import pygame
import time
import random

last_point = [0, 360]



def setup(screen, mvp):
    pass

def draw(screen, mvp):
    global last_point

    for i in range(0, 100) :
        seg(screen, mvp, i)   
    

def seg(screen, mvp, i):
    global last_point
    xoffset = 100
    y0 = screen.get_height() // 2
    y1 = (screen.get_height() // 2) + (mvp.audio_in[i] / 35)
    x = i * 10
    colorr = mvp.color_picker() #(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    color = (0,0,0)

    pygame.draw.rect(screen, colorr, [random.randrange(0,1280),random.randrange(0,720),5,5], 0)
    pygame.draw.circle(screen,colorr,(x + xoffset, y1),int(mvp.knob1 * 20), 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], int(mvp.knob2 * 20))
    last_point = [x + xoffset, y1]

