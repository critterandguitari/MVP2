import os
import pygame
import time
import random

def setup(screen, mvp):
    pass

note_down = False

def draw(screen, mvp):
    for i in range(0, 100) :
        seg(screen, mvp, i)    

def seg(screen, mvp, i) :
    
    x0 = 640
    x1 = 640 + (mvp.audio_in[i] / 35)
    y = i * 11
    bw = abs((mvp.audio_in[i] / 128))
    color = (bw, bw, bw)
    
    pygame.draw.circle(screen,color,(x1, y),40, 0)
   

