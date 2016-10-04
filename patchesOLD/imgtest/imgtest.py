import os
import pygame
import glob

images = []
image_index = 0

def setup(screen, mvp) :
    global images
    for filepath in sorted(glob.glob('../imgtest/*.jpg')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp) :
    global images, image_index
  
    if True:
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        screen.fill((0, 0, 0))
        rect = image.get_rect()
        screen.blit(image, rect)
