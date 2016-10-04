import os
import pygame
import time
import random
import glob

last_point = [0, 360]

images = []
image_index = 0

owen = 0


def setup(screen, mvp):
    global images
    #for filepath in sorted(glob.glob('../patches/imgtest/*.png')):
    for filepath in sorted(glob.glob('./web/static/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath).convert()
        images.append(img)

def draw(screen, mvp):
    global last_point, owen, image_index


    #owen = images[0]
    image_index += 1
    if image_index == len(images) : image_index = 0
    owen = images[image_index]

    owen = pygame.transform.scale(owen, (mvp.knob3 // 10,mvp.knob3 // 10))

    #screen.set_alpha(None)
    #owen.set_alpha(None)
    for i in range(0, 100) :
        seg(screen, mvp, i)   
    #last_point = [0, (screen.get_height() // 2)]

def seg(screen, mvp, i):
    global last_point, images, owen
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
    
    screen.blit(owen, (x + xoffset, y1))

