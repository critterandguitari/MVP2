import os
import pygame
import glob

images = []
image_index = 0

fall = 0
scoot = 0

bg = pygame.Surface((656,416))


#global waiting = 0 


def setup(screen, mvp) :
    global images, fall, bg
    #images = []
    
    bg = pygame.Surface((screen.get_width(),screen.get_height()))
    for filepath in sorted(glob.glob('../images/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        img = img.convert()
        images.append(img)



def draw(screen, mvp) :
    global images, image_index, fall, bg, scoot
    
    above = False
    
    #if waiting == 0 :
    for i in range(0, 100) :
        if abs(mvp.audio_in[i]) > 1000 :
            above = True
               # waiting = 4
    #else 
      #  waiting -= 1
  
    if above:
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        screen.blit(image, (0, 0))
