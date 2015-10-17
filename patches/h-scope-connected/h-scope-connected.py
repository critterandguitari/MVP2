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
    #last_point = [0, (screen.get_height() // 2)]

def seg(screen, mvp, i):
    global last_point
    xoffset = 100
    y0 = screen.get_height() // 2#random.randrange(0,1920)
    y1 = (screen.get_height() // 2) + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    x = i * 10#random.randrange(0,1080)
    #bw = random.randrange(0,255)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    
    pygame.draw.circle(screen,color,(x + xoffset, y1),4, 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], 2)
    last_point = [x + xoffset, y1]

