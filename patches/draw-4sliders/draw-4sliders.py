import os
import pygame
import time
import random

note_down = False

def setup(screen, mvp):
    pass


def draw(screen, mvp):
    
    
    length = int(mvp.knob2 * 1000)
    
    x = 10
    y = 10
    kwidth = screen.get_width() / 4
    xk1 = 0
    xk2 = kwidth
    xk3 = kwidth * 2
    xk4 = kwidth * 3
    y0 = screen.get_height()
    h =screen.get_height()
    
    kwidth = kwidth - 10
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk1, 0, kwidth, (mvp.knob1 * h) ], 0)
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk2, 0, kwidth, (mvp.knob2 * h) ], 0)
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk3, 0, kwidth, (mvp.knob3 * h) ], 0)
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk4, 0, kwidth, (mvp.knob4 * h) ], 0)


