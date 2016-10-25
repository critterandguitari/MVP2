import os
import pygame
import glob


images = []
image_index = 0

bg = pygame.Surface((656,416))

def setup(screen, mvp) :
    global images
    #for filepath in sorted(glob.glob('../patches/imgtest/*.JPG')):
    for filepath in sorted(glob.glob('../patches/ImageAlphaTest/gt/*.JPG')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp) :
    global images, image_index, bg
  
    if True: #mvp.note_on:
        print 'note is on' 
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        #screen.fill((0, 0, 0))
        rect = image.get_rect()
        #image.set_alpha(5) #this works
        #image.set_colorkey((range(0,250), range(0,100), range(0,100)))
        #image.set_colorkey((230, 230, 230))
        image.set_colorkey((int(mvp.knob1*255), int(mvp.knob2*255), int(mvp.knob3*255),))
        bg.blit(image, rect)
        screen.blit(bg, rect)
