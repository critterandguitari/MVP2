import os
import pygame
import time
import random

note_down = False
count = 0

def draw(screen, mvp):
    
    
    length = mvp.knob2#random.randrange(100,255)
    
    x = 10
    y = 10
    kwidth = int(screen.get_width() * float(mvp.knob2 / 1024))
    xk1 = 0
    xk2 = kwidth
    xk3 = kwidth * 2
    xk4 = kwidth * 3
    y0 = screen.get_height()
    h =screen.get_height()
    
    kwidth = kwidth - 10
    
    # convert knob to 0-1
    c = float(mvp.knob4) / 1024

    color = mvp.color_picker()
        
    pygame.draw.line(screen, color, [screen.get_width() / 2, y0], [screen.get_width() / 2 + mvp.knob3, y0 - ((float(mvp.knob1) / 1024) * h) ], mvp.knob2)


    global count

        
    h = screen.get_height()
    w =screen.get_width()
    

    
    if mvp.note_on :
        count += 1
        if count > 100 :
            count = 0
        x = count * (w / 100)
        mvp.brightness = 1
        color = mvp.color_picker()
        offset = mvp.knob1
        pygame.draw.line(screen, color, [x, mvp.note_num * 2 + mvp.knob3 + offset], [x + mvp.knob2, mvp.note_num * 2 + offset], 20)
    

    #pygame.draw.line(screen, color, [xk1 + kwidth / 2, y0], [xk1 + kwidth / 2, y0 - ((float(mvp.knob1) / 1024) * h) ], kwidth)

        

    
    #color = ( thing, thing2, thing3 )
    
    #pygame.draw.line(screen, color, [xk1 + kwidth / 2, y0], [xk1 + kwidth / 2, y0 - ((float(mvp.knob1) / 1024) * h) ], kwidth)
    
  #  pygame.draw.line(screen, color, [xk2 + kwidth / 2, y0], [xk2 + kwidth / 2, y0 - ((float(mvp.knob2) / 1024) * h) ], kwidth)

  #  pygame.draw.line(screen, color, [xk3 + kwidth / 2, y0], [xk3 + kwidth / 2, y0 - ((float(mvp.knob3) / 1024) * h) ], kwidth)
    
  #  pygame.draw.lie(screen, color, [xk2, y0], [xk1, x + mvp.knob1 // 2, ], kwidth)
   # pygame.draw.line(screen, color, [xk3, y0], [xk1, x + mvp.knob1 // 2, ], kwidth)
    #pygame.draw.line(screen, color, [xk4, y0, [xk1, x + mvp.knob1 // 2, ], kwidth)


