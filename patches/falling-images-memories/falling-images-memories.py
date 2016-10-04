import os
import pygame
import glob

images = []
image_index = 0

fall = 0
scoot = 0

bg = pygame.Surface((656,416))


def setup(screen, mvp) :
    global images, fall, bg
    
    bg = pygame.Surface((screen.get_width(),screen.get_height()))
    for filepath in sorted(glob.glob('../images/*.jpg')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp) :
    global images, image_index, fall, bg, scoot
  
    if True:
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        screen.blit(image, (0, 0))
