import os
import pygame
import time
import random

count = 0
background = pygame.Surface((1,1))

def setup(screen, mvp):
    global background
    background = pygame.Surface(screen.get_size())
    background.set_colorkey((255,0,255))


def draw(screen, mvp):
    global count, background
        #screen.fill( (1,99,1))
    above = False
    for i in range(0, 100) :
        if abs(mvp.audio_in[i]) > 1000 :
            above = True
        
    if above :#mvp.note_on :
        count += 1
#        if count > mvp.knob1 // 10 : 
#            count = 0
#            screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        x=screen.get_width() / 2#random.randrange(0,screen.get_width())
        y=screen.get_height() / 2#random.randrange(0,screen.get_height())
        pos = (x,y)
        
        font = pygame.font.Font("../patches/Quivira.ttf", int(mvp.knob2 * 1000))
        
        unistr = get_unicode_character(int(mvp.knob3 * 12))
        text = font.render(unistr, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        textpos = text.get_rect()
        textpos.centerx = random.randrange(0,screen.get_width())
        textpos.centery = random.randrange(0,screen.get_height())
        background.blit(text, textpos)
    else :
        background.fill((255,0,255))
    
    
    screen.blit(background, (0,0))
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
        

