import pygame
from pygame.locals import *
from Pieces import *
'''
THIS WAS AMDE BY RICHARD AND OLIVER :)
'''

pygame.init()
white,black = (255,255,255),(0,0,0)

lead_x = 20
lead_y = 20

#Create a displace surface object
DISPLAYSURF = pygame.display.set_mode((0, 0), RESIZABLE)


mainLoop = True



while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

        elif event.type == pygame.VIDEORESIZE:
            scrsize = event.size
            width   = event.w
            hight   = event.h
            screen = pygame.display.set_mode(scrsize,RESIZABLE)
            changed = True

    w, h = pygame.display.get_surface().get_size()
    #print (w,h)
    DISPLAYSURF.fill(white)

    WSize = w/8
    HSize = h/8

    chess = [[0,1,0,1,0,1,0,1,0],
             [1,0,1,0,1,0,1,0,1],
             [0,1,0,1,0,1,0,1,2],
             [1,0,1,0,1,0,1,0,3],
             [0,1,0,1,0,1,0,1,4],
             [1,0,1,0,1,0,1,0,5],
             [0,1,0,1,0,1,0,1,6],
             [1,0,1,0,1,0,1,0,7]]

    for y in chess:
        for x in range(len(chess[chess.index(y)])-1):
            #print(chess.index(y))
            if y[x] == 0:
                XPos = WSize*(x)
                YPos = HSize*(chess.index(y))
                #print(XPos,YPos)

                pygame.draw.rect(DISPLAYSURF, (0,0,0),(XPos,YPos,WSize,HSize))
    for i in range(8):
        XPos = i* WSize
        YPos = 6* HSize
        image=DISPLAYSURF.blit(pygame.image.load(pawnsW[i].image),(XPos,YPos))
        pygame.transform.scale(image,WSize,HSize)

    pygame.display.update()




pygame.quit()
