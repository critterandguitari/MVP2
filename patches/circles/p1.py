import os
import pygame
import time
import random

def test(t):
    print t

def draw(screen):

    #s = serialport.read(1)
    font = pygame.font.Font("../patches/Quivira.ttf", 320)
    #unistr = unichr(random.choice((0x0000, 0xFF00)) + random.randint(0, 0xff))
    unistr = unichr(random.randint(0x01400, 0x015b0))
    text = font.render(unistr, True, (random.randint(0,255), random.randint(0,255), random.randint(0,255) ))
    screen.blit(text, (10, 10))
    time.sleep(.05)

