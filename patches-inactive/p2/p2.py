import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    
    global note_down

    if mvp.note_on :
        note_down = True
        print note_down
    if mvp.note_off :
        note_down = False
        print note_down

    if note_down :
        x=random.randrange(0,656)
        y=random.randrange(0,400)
        y1=random.randrange(0,400)
        x1=random.randrange(0,656)
        size = random.randrange(0,200)
        width = mvp.knob2#random.randrange(100,255)
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        pygame.draw.line(screen, color, [x, y], [x1, y1], width)


