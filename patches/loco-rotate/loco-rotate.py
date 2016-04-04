import os
import pygame
import time
import random

last_point = [0, 360]

angle = 0

rotated = None#pygame.Surface(1280, 720)

def setup(screen, mvp):
    global rotated
    rotated = pygame.Surface((1280, 720))
    

def draw(screen, mvp):
    global last_point, rotated, angle
    #screen.fill( (countr, countg, countb))
    #rotated.fill( (255, 250, 250))

    for i in range(0, 100) :
        seg(rotated, mvp, i)   
    #last_point = [0, (screen.get_height() // 2)]
    angle += 47
    angle %= 360
    screen.blit(pygame.transform.rotate(rotated, angle), (0,0))
    

def seg(screen, mvp, i):
    global last_point
    xoffset = 100
    y0 = screen.get_height() // 2#random.randrange(0,1920)
    y1 = (screen.get_height() // 2) + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    x = i * 10#random.randrange(0,1080)
    #bw = random.randrange(0,255)
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    #color = (0,0,0)

    
    pygame.draw.circle(screen,color,(x + xoffset, y1),mvp.knob1 // 50, 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], mvp.knob2 // 50)
    last_point = [x + xoffset, y1]

