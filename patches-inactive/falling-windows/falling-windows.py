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
    for filepath in sorted(glob.glob('../patches/ImageAlphaTest/gt/*.JPG')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp) :
    global images, image_index, fall, bg, scoot
  
    if mvp.note_on:
        fall += mvp.knob1 // 10
        scoot += mvp.knob2 // 10
        if fall > screen.get_height() : fall = 0
        if scoot > screen.get_width() : scoot = 0
        
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        screen.fill((0, 0, 0))
        rect = image.get_rect()
        rect.centery += fall
        rect.centerx += scoot
        image.set_colorkey((0,0,0))
        bg.blit(image, rect)
        rect = bg.get_rect()
        screen.blit(bg, rect)
