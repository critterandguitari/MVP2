import os
import pygame
import time
import random

def draw(screen, mvp):

    if mvp.note_on :
        font = pygame.font.Font("../patches/Quivira.ttf", mvp.knob1 // 2)
        
        # all of them (or a lot of them...)
        #unistr = unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
        
        # aboriginal set :
        unistr = unichr(random.randint(0x01400, 0x015b0))
        
        text = font.render(unistr, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
        screen.blit(text, (mvp.knob3 // 2, mvp.knob2 // 2))

