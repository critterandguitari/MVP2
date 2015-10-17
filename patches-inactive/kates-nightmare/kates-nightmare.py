import os
import pygame
import time
import random
import glob

last_point = [0, 360]

images = []
image_index = 0

def setup(screen, mvp):
    global images
    for filepath in sorted(glob.glob('../patches/imgtest/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert()
        images.append(img)

def draw(screen, mvp):
    global last_point
    #screen.fill( (countr, countg, countb))
    screen.fill( (255, 250, 250))

    for i in range(0, 100) :
        seg(screen, mvp, i)   
    #last_point = [0, (screen.get_height() // 2)]

def seg(screen, mvp, i):
    global last_point, images
    xoffset = 100
    y0 = screen.get_height() // 2#random.randrange(0,1920)
    y1 = (screen.get_height() // 2) + (mvp.audio_in[i] / 35)#random.randrange(0,1920)
    x = i * 10#random.randrange(0,1080)
    #bw = random.randrange(0,255)
    colorr = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    color = (0,0,0)

    pygame.draw.rect(screen, colorr, [0,0,20,20], 0)
    pygame.draw.circle(screen,color,(x + xoffset, y1),mvp.knob1 // 50, 0)
    pygame.draw.line(screen, color, last_point, [x + xoffset, y1], mvp.knob2 // 50)
    last_point = [x + xoffset, y1]
    
    image = images[0]
    rect = image.get_rect()
    screen.blit(image, (x + xoffset, y1))

