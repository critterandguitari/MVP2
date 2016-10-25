import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

def draw(screen, mvp):

    if True: #mvp.note_on :
        font = pygame.font.Font("../patches/Quivira.ttf", int(mvp.knob1 * 500))
        
        # all of them (or a lot of them...)
        #unistr = unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
        
        # aboriginal set :
        unistr = unichr(random.randint(0x01400, 0x015b0))
        
        text = font.render(unistr, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        screen.blit(text, (int(mvp.knob3 * 1300 - 100), int(mvp.knob2 * 750 - 150))) 
        #the subtracted numbers print the letters outside top and left edges

