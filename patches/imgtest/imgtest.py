import os
import pygame
import glob
import random

images = []
image_index = 0

def setup(screen, mvp) :
    global images
    for filepath in sorted(glob.glob('../patches/imgtest/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp) :
    global images, image_index
  
    if mvp.note_on:
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        #screen.fill((0, 0, 0))
        rect = image.get_rect()
        #screen.blit(image, (random.randrange(0,screen.get_width()),random.randrange(0,screen.get_height())))
        screen.blit(pygame.transform.scale(pygame.transform.rotate(image, mvp.knob1 // 3), (mvp.knob3, mvp.knob4)), (mvp.knob2 // 3,mvp.knob3 // 3) )

