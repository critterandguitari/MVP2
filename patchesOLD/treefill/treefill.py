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
    for filepath in sorted(glob.glob('../patches/treefill/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp):
    if mvp.quarter_note :
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        screen.fill(color) 
    

    if mvp.note_on :
        x=random.randrange(0,700)
        y=random.randrange(0,400)
        size = mvp.knob2
        color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        width = mvp.knob1 // 50
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

