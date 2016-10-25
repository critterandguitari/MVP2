import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

note_down = False
count = 0

def draw(screen, mvp):
    
    
    length = int(mvp.knob2*1000)
    
    x = 10
    y = 10
    kwidth = int(screen.get_width() * int(mvp.knob2))
    xk1 = 0
    xk2 = kwidth
    xk3 = kwidth * 2
    xk4 = kwidth * 3
    y0 = screen.get_height()
    h =screen.get_height()
    
    kwidth = kwidth - 10
    
    # convert knob to 0-1
    c = int(mvp.knob4)

    color = mvp.color_picker()
        
    pygame.draw.line(screen, color, [640, y0], [640 + int(mvp.knob3*1000), y0 - int(mvp.knob1 * 1000) * h], int(mvp.knob2 * 1000))


    global count

        
    h = screen.get_height()
    w =screen.get_width()
    

    
    if True: #mvp.note_on :
        count += 1
        if count > 100 :
            count = 0
        x = count * (w / 100)
        mvp.brightness = 1
        color = mvp.color_picker()
        offset = int(mvp.knob1*1000)
        pygame.draw.line(screen, color, [x, mvp.note_num * 2 + int(mvp.knob3*1000) + offset], [x + int(mvp.knob2*1000), mvp.note_num * 2 + offset], 20)
    


