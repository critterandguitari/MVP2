import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

note_down = False
count = 0

def draw(screen, mvp):
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
        offset = int(mvp.knob1 * 1000)
        pygame.draw.line(screen, color, [x, mvp.note_num * 2 + int(mvp.knob3*1000) + offset], [x + mvp.knob2, mvp.note_num * 2 + offset], 20)
    


  #  pygame.draw.lie(screen, color, [xk2, y0], [xk1, x + mvp.knob1 // 2, ], kwidth)
   # pygame.draw.line(screen, color, [xk3, y0], [xk1, x + mvp.knob1 // 2, ], kwidth)
    #pygame.draw.line(screen, color, [xk4, y0, [xk1, x + mvp.knob1 // 2, ], kwidth)


