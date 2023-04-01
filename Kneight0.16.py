#Test RPG by David Sun
#December 31, 2022
#This has no copyright information. I created it by myself. 

import pygame
pygame.init()

win = pygame.display.set_mode((2475,2000))
pygame.display.set_caption("Kneight's Life Vol. 0.16")

x = 0
y = 0

vel = 10
#controls speed
playerImg = pygame.image.load('Kneight200x200pix.jpg')
bg = pygame.image.load("BGKneight'sPathLarger.jpg")
win.blit(cImg, (0,0))
while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    win.blit(bg,(0,0))
    win.blit(playerImg,(x,y))   
    pygame.display.update() 
    
pygame.quit()
