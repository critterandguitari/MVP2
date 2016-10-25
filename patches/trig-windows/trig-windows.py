import os
import pygame
import time
import random

offset = 0

def setup (screen, mvp) :
    pass

def draw(screen, mvp):
        
    global offset
    
    if True: #mvp.note_on :
    
        num = int(mvp.knob1 * 10)
        
        num += 1
    
        width = screen.get_width() // num 
        width = width // 2
    
        offset += int(mvp.knob2 *10)
        if offset > width : offset = 0
    
        length = mvp.knob2#random.randrange(100,255)
    
        color = pygame.Color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), 255)
        
        saturation = int(mvp.knob3 * 100)
        if saturation > 100 : saturation = 100
        value =  int(mvp.knob4 * 100)
        if value > 100 : value = 100
        
       # color.hsva = (color.hsva[0], saturation, value, 100)
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        
    
        h = screen.get_height()
        w = screen.get_width()
    
        offsetx = offset
        offsety = offset
        for x in range(0, num) :
            pygame.draw.line(screen, color, [x * width * 2 + width / 2 + offsetx, 0+offsety], [x * width * 2 + width / 2 + offsetx, h+offsety], width)
        
        width = screen.get_height() // num 
        width = width // 2
        for y in range(0, num) :
            pygame.draw.line(screen, color, [0 + offsetx, y * width * 2 + width / 2 + offsety], [w + offsetx, y * width * 2 + width / 2+ offsety], width)
    
    

