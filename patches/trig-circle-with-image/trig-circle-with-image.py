import os
import pygame
import time
import random
import glob

images = []
image_index = 0
count = 0

def setup(screen, mvp):
    global images
    for filepath in sorted(glob.glob('../images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp):
    if mvp.quarter_note :
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        screen.fill(color) 
    

    if True: #mvp.note_on :
        x=(random.randrange(0,1400) - 100)
        y=(random.randrange(0,800) - 50)
        size = int(mvp.knob2*1000)
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = int(mvp.knob1 *20)
        if width == 0 : width = 1
        if width > size : width = size
        pygame.draw.circle(screen,color,[x,y],size, 0)
        global images
        global count, image_index
        count += 1
        if count > 8 :
            count = 0
        
            image_index += 1
            if image_index == len(images) : image_index = 0
        image = images[image_index]
        rect = image.get_rect()
        screen.blit(image, rect)  

