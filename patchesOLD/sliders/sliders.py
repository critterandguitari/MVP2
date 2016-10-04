import os
import pygame
import time
import random

note_down = False

def draw(screen, mvp):
    
    
    length = mvp.knob2#random.randrange(100,255)
    
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
    pygame.draw.rect(screen, color, [xk1, 0, kwidth, ((float(mvp.knob1) / 1024) * h) ], 0)
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk2, 0, kwidth, ((float(mvp.knob2) / 1024) * h) ], 0)
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk3, 0, kwidth, ((float(mvp.knob3) / 1024) * h) ], 0)
    
    color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    pygame.draw.rect(screen, color, [xk4, 0, kwidth, ((float(mvp.knob4) / 1024) * h) ], 0)
  #  pygame.draw.lie(screen, color, [xk2, y0], [xk1, x + mvp.knob1 // 2, ], kwidth)
   # pygame.draw.line(screen, color, [xk3, y0], [xk1, x + mvp.knob1 // 2, ], kwidth)
    #pygame.draw.line(screen, color, [xk4, y0, [xk1, x + mvp.knob1 // 2, ], kwidth)


