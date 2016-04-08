import os
import pygame
import glob
import random

images = []
image_index = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

def setup(screen, mvp) :
    global images
    #for filepath in sorted(glob.glob('../patches/imgtest/*.png')):
    for filepath in sorted(glob.glob('/usbdrive/Images/flowers/*.png')):
        filename = os.path.basename(filepath)
        print 'loading image file: ' + filename
        img = pygame.image.load(filepath)
        images.append(img)



def draw(screen, mvp) :
    global images, image_index, count1, count2, count3, count4
  
  
    above = False
    for i in range(0, 100) :
        if abs(mvp.audio_in[i]) > 2000 :
            above = True
    
    if above :
        #color = (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
        #screen.fill((0,0,0))
  
        count1 += (mvp.knob1 // 10) + 1
        count2 += (mvp.knob2 // 10) + 1
        count3 += (mvp.knob3 // 10) + 1
        count4 += (mvp.knob4 // 10) + 1
        
    
        image_index += 1
        if image_index == len(images) : image_index = 0
        image = images[image_index]
        #screen.fill((0, 0, 0))
        rect = image.get_rect()
        #screen.blit(pygame.transform.scale(pygame.transform.rotate(image, mvp.knob1 // 3), (mvp.knob3, mvp.knob4)), (mvp.knob2 // 3,mvp.knob3 // 3) )
        #screen.blit(pygame.transform.scale(pygame.transform.rotate(image, (count1 % 1024) // 3), ((count2 % 1024), (count3 % 1024))), ((count4 % 1024) // 3,mvp.knob3 // 3) )
        screen.blit(pygame.transform.scale(pygame.transform.rotate(image, (count1 % 1024) // 3), ((count2 % 1024), (count3 % 1024))), ((count4 % 1024) // 3,mvp.knob3 // 3) )

    
