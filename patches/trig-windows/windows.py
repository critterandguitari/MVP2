import os
import pygame
import time
import random

offset = 0

def setup (screen, mvp) :
    pass

def draw(screen, mvp):
        
    global offset
    
    if mvp.note_on :
    
        num = mvp.knob1 // 100
        
        num += 1
    
        width = screen.get_width() // num 
        width = width // 2
    
        offset += mvp.knob2 // 100
        if offset > width : offset = 0
    
        length = mvp.knob2#random.randrange(100,255)
    
        color = pygame.Color(random.randrange(0,255), random.randrange(0,255), random.randrange(0,255), 255)
        
        saturation = mvp.knob3 // 10
        if saturation > 100 : saturation = 100
        value =  mvp.knob4 // 10
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
    
    

