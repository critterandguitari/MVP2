import os
import pygame
import time
import random
import serial
import fullfb
import glob
import imp
import socket
import traceback
import sys

import liblo

from pygame.locals import *

import alsaaudio, audioop
 


pygame.init()


print "opening frame buffer"
screen = fullfb.init()

while 1:

    # quit on esc
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()

    screen.fill( (random.randint(0,255), random.randint(0,255), random.randint(0,255))) 

    pygame.display.flip()
    

time.sleep(1)


print "Quit"
