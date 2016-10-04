import os
import pygame
import time
import random

count = 0

def setup(screen, mvp):
    pass

def draw(screen, mvp):
    global count

    
    if count > 4 : 
        count = 0
        screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        #screen.fill( (1,99,1))
        

    if mvp.note_on :
        count += 1
        x=random.randrange(0,screen.get_width())
        y=random.randrange(0,screen.get_height())
        
        font = pygame.font.Font("../patches/Quivira.ttf", 200)
        
        unistr = unichr(random.randint(32, 127))
        
        # all of them (or a lot of them...)
        #unistr = unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
        
        # aboriginal set :
        #unistr = unichr(random.randint(0x01400, 0x015b0))
        
        # ogham
        #unistr = unichr(random.randint(0x1680, 0x169C))
        
        # arrows
        #unistr = unichr(random.randint(0x2190, 0x21FF))
        
        # math
        #unistr = unichr(random.randint(0x2200, 0x22ff))
        
        # geometric shapes
        #unistr = unichr(random.randint(0x25a0, 0x25ff))
        
        # box drawing
        #unistr = unichr(random.randint(0x2500, 0x257f))
        
        # Brail
        #unistr = unichr(random.randint(0x2800, 0x28FF))
        
        # More math
        #unistr = unichr(random.randint(0x2A00, 0x2ADF))
        
        # from math -- sharp symbols
        #unistr = unichr(random.randint(0x2A80, 0x2ABC))

        # more arrows
        #unistr = unichr(random.randint(0x2900, 0x297F))
        
        #chess
        #unistr = unichr(random.randint(0xE010, 0xE04F))
        
        #Genji-mon Symbols
        #unistr = unichr(random.randint(0xF500, 0xF535))
        
        # dominos  ? doesn't work
        #unistr = unichr(random.randint(0x1F030, 0x1F09F))
        
        # emoticons -- doesn't work ?!?!
        #unistr = unichr(random.randint(0x1F600, 0x1F64F))
        #unistr = unichr(int(0x1F600))
        
    

        
        text = font.render(unistr, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        screen.blit(text, (x, y))
        
        #time.sleep(.05)

