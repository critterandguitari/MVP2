import os
import pygame
import time
import random

count = 0
count2 = 0
size = 0

def setup(screen, mvp):
    pass

def draw(screen, mvp):
    global count, size
        #screen.fill( (1,99,1))
        
    if mvp.note_on :
        count += 1
        if count > mvp.knob1 // 10 : 
            count = 0
            screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
            
        size += mvp.knob2 // 4
        
        if size > 700:
            size = 0
            
        x=screen.get_width() / 2#random.randrange(0,screen.get_width())
        y=screen.get_height() / 2#random.randrange(0,screen.get_height())
        pos = (x,y)
        
        font = pygame.font.Font("../patches/Quivira.ttf", size)
        

        
        unistr = get_unicode_character(int((float(mvp.knob3) / 1024) * 12))
        
        text = font.render(unistr, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        
        screen.blit(text, textpos)
        
        #time.sleep(.05)

def get_unicode_character(set) :
    
    if set == 0 :
        # all of them (or a lot of them...)
        return unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
        
    if set == 1 :
        # ogham
        return unichr(random.randint(0x1680, 0x169C))
        
    if set == 2 :
        # arrows
        return unichr(random.randint(0x2190, 0x21FF))
        
    if set == 3 :
        # math
        return unichr(random.randint(0x2200, 0x22ff))
        
    if set == 4 :
        # geometric shapes
        return unichr(random.randint(0x25a0, 0x25ff))
        
    if set == 5 :
        # box drawing
        return unichr(random.randint(0x2500, 0x257f))
        
    if set == 6 :
        # Brail
        return unichr(random.randint(0x2800, 0x28FF))
        
    if set == 7 :
        # More math
        return unichr(random.randint(0x2A00, 0x2ADF))
        
    if set == 8 :
        # from math -- sharp symbols
        return unichr(random.randint(0x2A80, 0x2ABC))

    if set == 9 :
        # more arrows
        return unichr(random.randint(0x2900, 0x297F))
    
    if set == 10 :
        #chess
        return unichr(random.randint(0xE010, 0xE04F))
        
    if set == 11 :
        #Genji-mon Symbols
        return unichr(random.randint(0xF500, 0xF535))
        

