import pygame
from pygame.locals import *
from Pieces import*
from Moves import*
#Check mate checker
#pawn take diagonal yaaa yeet
#valid and invalid moves
pygame.init()
white,black,red = (220,220,220),(0,0,0),(0,255,0) #Colours the board

lead_x = 20
lead_y = 20

MARGIN = 0
#Create a displace surface object
#Allows for a resizeable window
DISPLAYSURF = pygame.display.set_mode((800, 800), RESIZABLE)
pygame.display.set_caption("Chess in Python")

mainLoop = True
Turn = "W"

'''creating pieces'''
pawnsW=[]
pawnsB=[]
RookB=[]
RookW=[]
KnightW=[]
KnightB=[]
BishopW=[]
BishopB=[]
#Creates 8 pawns of each colour
for i in range(8) :
    newWPawn = pawn("white")
    pawnsW.append(newWPawn)
    newBPawn = pawn("black")
    pawnsB.append(newBPawn)
#Creates 2 Rooks, Knights, Bishop of each colour
for i in range(2):
    newWRook = rook("white")
    RookW.append(newWRook)

    newBRook = rook("black")
    RookB.append(newBRook)

    newWKnight = knight("white")
    KnightW.append(newWKnight)

    newBKnight = knight("black")
    KnightB.append(newBKnight)

    newWBishop = bishop("white")
    BishopW.append(newWBishop)

    newBBishop = bishop("black")
    BishopB.append(newBBishop)

#Creates a King and Queen of each colour
newWQueen = queen("white")

newBQueen = queen("Black")

newWKing = king("white")

newBKing = king("black")
#Board being drawn
chess = [[[0,"BR"],[1,"BKn"],[0,"BB"],[1,"BK"],[0,"BQ"],[1,"BB"],[0,"BKn"],[1,"BR"],[0,0]],
        [[1,"BP"],[0,"BP"],[1,"BP"],[0,"BP"],[1,"BP"],[0,"BP"],[1,"BP"],[0,"BP"],[1,0]],
        [[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[2,0]],
        [[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[3,0]],
        [[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[4,0]],
        [[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[1,0],[0,0],[5,0]],
        [[0,"WP"],[1,"WP"],[0,"WP"],[1,"WP"],[0,"WP"],[1,"WP"],[0,"WP"],[1,"WP"],[6,0]],
        [[1,"WR"],[0,"WKn"],[1,"WB"],[0,"WK"],[1,"WQ"],[0,"WB"],[1,"WKn"],[0,"WR"],[7,0]]]

column = None
row = None
Tile = None

#Piece moves
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
            
        elif event.type == pygame.MOUSEBUTTONDOWN and column != None:
             pos = pygame.mouse.get_pos()
             Newcolumn= pos[0] // (WSize + MARGIN)
             Newrow = pos[1] // (HSize + MARGIN)
             Newrow = int(Newrow)
             Newcolumn = int(Newcolumn)
             if Tile == 0:
                 Tile == None
                 chess[row][column][0] = 0
                 
             else:
                 Tile == None
                 chess[row][column][0] = 1
             
             if chess[Newrow][Newcolumn][1] == 0:
                 
                 if (Move(Piece,row,Newrow,column,Newcolumn,chess)) == True:
                     chess[row][column][1] = 0
                     chess[Newrow][Newcolumn][1] = Piece
                     if Turn == "W":
                         Turn = "B"
                     else:
                         Turn = "W"
                     
             elif chess[row][column][1][0] != chess[Newrow][Newcolumn][1][0]:
                 print(Move(Piece,row,Newrow,column,Newcolumn,chess))
                 if (Move(Piece,row,Newrow,column,Newcolumn,chess)) == True:
                     chess[row][column][1] = 0
                     chess[Newrow][Newcolumn][1] = Piece

                     if Turn == "W":
                         Turn = "B"
                     else:
                         Turn = "W"
             
             column = None
             row = None
             
            
                                  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WSize + MARGIN)
            row = pos[1] // (HSize + MARGIN)
            #Displays Coordinate and shows piece
            print("Click ", "Grid coordinates:",row,column)
            column = int(column)
            row = int(row)
            Piece =(chess[row][column][1])
            print(Piece ,column,row)
            
            if chess[row][column][0] == 0:
                Tile = 0
            if chess[row][column][0] == 1:
                Tile = 1
                
            chess[row][column][0] = 2
            print(chess[row][column][0])
            
            if Piece == 0:
                chess[row][column][0] = Tile
                column = None
                row = None
                Tile= None
                
            elif chess[row][column][1][0] != Turn:
                chess[row][column][0] = Tile
                column = None
                row = None
                Tile= None
            
                

    w, h = pygame.display.get_surface().get_size()
    #print (w,h)
    DISPLAYSURF.fill(white)

    WSize = w/8
    HSize = h/8



    for y in chess:
        i=0
        for x in chess[chess.index(y)]:
            #print (x)
            #print(chess.index(y))
            #print(x[0])
            
            if x[0] == 1:
                
                XPos = (w/8)*(i)
                YPos = (h/8)*(chess.index(y))
                #print(XPos)
                #print(YPos)
                #print(XPos,YPos)
                

                pygame.draw.rect(DISPLAYSURF, (0,0,0),(XPos,YPos,WSize,HSize))
            elif x[0] == 2:
                XPos = (w/8)*(i)
                YPos = (h/8)*(chess.index(y))
                #print(XPos)
                #print(YPos)
                #print(XPos,YPos)
                

                pygame.draw.rect(DISPLAYSURF, (0,255,0),(XPos,YPos,WSize,HSize))
                
            i = i+1
            #print(i)

    
    for y in chess:
        #variables are defined
        i=0
        rb=0
        rw=0
        knw=0
        knb=0
        bw=0
        bb=0
        for x in chess[chess.index(y)]:
            #print(x)
            XPos = (w/8)*(i)
            YPos = (h/8)*(chess.index(y))

            #Placing Pawn
            if x[1] == "WP":
                pieces = pygame.image.load(pawnsW[i].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
            elif x[1] == "BP":
                pieces = pygame.image.load(pawnsB[i].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))

            #Placing Rooks    
            elif x[1] == "BR":
                pieces = pygame.image.load(RookB[rb].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
                rb = rb +1
            elif x[1] == "WR":
                pieces  = pygame.image.load(RookW[rw].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
                rw = rw +1

            #Placing Knights
            elif x[1] == "WKn":
                pieces  = pygame.image.load(KnightW[knw].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
                knw = knw +1

            elif x[1] == "BKn":
                pieces  = pygame.image.load(KnightB[knw].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
                knb = knb +1

            #Placing Bishops
            elif x[1] == "WB":
                pieces  = pygame.image.load(BishopW[bw].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
                bw = bw +1
            elif x[1] == "BB":
                pieces  = pygame.image.load(BishopB[bb].image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
                bb = bb +1

            #Placing Queens
            elif x[1] == "WQ":
                pieces  = pygame.image.load(newWQueen.image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
            elif x[1] == "BQ":
                pieces  = pygame.image.load(newBQueen.image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))

            #Placing Kings
            elif x[1] == "WK":
                pieces  = pygame.image.load(newWKing.image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos))
            elif x[1] == "BK":
                pieces  = pygame.image.load(newBKing.image)
                pieces = pygame.transform.scale(pieces,(int(WSize),int(HSize)))
                DISPLAYSURF.blit(pieces,(XPos,YPos)) 
            i = i +1
    
    pygame.display.update()

#range(len(chess[chess.index(y)])-1)

    
    #print(chess[1][0][1])
pygame.quit()
