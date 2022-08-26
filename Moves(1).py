#Fix King Move Multiple diagonal and knight move yeet
#Rook  NOT vertical +1 -1 yeet
#Bishop  NOT 1 diagonal yeet
#Queen OPPOSITE King yeet
#change pw to wp to make taking yeet
#King box turn red when in check

def Check(chess,Turn):
    if Turn = "W":
        Enemy="B"
    else:
        Enemy = "W"
    King = Turn + "K"
    for y in chess:
        for x in y:
            if x[1] == King:
                Ypos = chess.index(y)
                Xpos = y.index(y)
    NewY=Ypos
    NewX=Xpos
    Check = False
    while NewY=<6:
        NewY = NewY+1
        if chess[NewY][NewX][1] == Enemy + "Q" or chess[NewY][NewX][1] == Enemy + "R":
            Check = True
    while NewY=>1:
        NewY = NewY-1
        if chess[NewY][NewX][1] == Enemy + "Q" or chess[NewY][NewX][1] == Enemy + "R":
            Check = True
    while NewX=<6:
        NewX = NewX+1
        if chess[NewY][NewX][1] == Enemy + "Q" or chess[NewY][NewX][1] == Enemy + "R":
            Check = True
    while NewX=>1:
        NewX = NewX-1
        if chess[NewY][NewX][1] == Enemy + "Q" or chess[NewY][NewX][1] == Enemy + "R":
            Check = True
    while NewY =>1 or NewX =>1
    
def Move(Piece,Ypos,NewY,Xpos,NewX,chess):
    if Piece == "BK":
        if KingMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "BQ":
        if  QueenMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "BB":
        if  BishopMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "BKn":
        if  KnightMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "BR":
        if  RookMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "BP":
        if  PawnMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "WK":
        if  KingMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "WQ":
        if  QueenMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "WB":
        if  BishopMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "WKn":
        if  KnightMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "WR":
        if  RookMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    elif Piece == "WP":
        if PawnMove(Ypos,NewY,Xpos,NewX,chess) == True:
            return True
    return False
        

def sign(z): #Shows the direction of the moves
    if z >= 0:
        return 1
    else:
        return -1
            

def BishopMove(Ypos,NewY,Xpos,NewX,chess):
    if Ypos!=NewY and NewX!=Xpos and abs(Ypos-NewY) ==abs(Xpos-NewX):#Condition for the bishop move
        DirectionY = sign(NewY-Ypos)
        DirectionX = sign(NewX-Xpos)
        x,y = Xpos + DirectionX, Ypos + DirectionY
        while x !=NewX and y !=NewY:#This checks if they are any spaces on the board
            
            if chess[y][x][1]:#empty space
                return False
            x +=DirectionX
            y +=DirectionY
        return True
    return False

def RookMove(Ypos,NewY,Xpos,NewX,chess):
    #print("running")
    if (Ypos == NewY) ^ (Xpos == NewX):
        #print("test")
        if  Xpos == NewX:
            DirectionY = sign(NewY-Ypos)
            y = Ypos + DirectionY
            print (y)
            print (NewY)
            while y !=NewY:
                
                if chess[y][Xpos][1]:#empty space
                    return False
                y +=DirectionY
            return True

        else:
            print(Xpos,NewX)
            DirectionX= sign(NewX-Xpos)
            x = Xpos + DirectionX
            print(x)
            while x !=NewX:
                if chess[Ypos][x][1]:#empty space
                    return False
                x +=DirectionX     
            return True
    return False

def KnightMove(Ypos,NewY,Xpos,NewX,chess):
    if ((NewX == Xpos + 2 or NewX == Xpos - 2) and (NewY == Ypos + 1 or NewY == Ypos - 1))^ ((NewY == Ypos + 2 or NewY == Ypos - 2) and (NewX == Xpos + 1 or NewX == Xpos - 1)):
        return True
    return False
def QueenMove(Ypos,NewY,Xpos,NewX,chess):
    if Ypos!=NewY and NewX!=Xpos and abs(Ypos-NewY) ==abs(Xpos-NewX):#Condition for the bishop move
        DirectionY = sign(NewY-Ypos)
        DirectionX = sign(NewX-Xpos)
        x,y = Xpos + DirectionX, Ypos + DirectionY
        while x !=NewX and y !=NewY:#This checks if they are any spaces on the board
            if chess[y][x][1]:#empty space
                return False
            x +=DirectionX
            y +=DirectionY
        return True
    
    elif (Ypos == NewY) ^ (Xpos == NewX):
        #print("test")
        if  Xpos == NewX:
            DirectionY = sign(NewY-Ypos)
            y = Ypos + DirectionY
            while y !=NewY:
                if chess[y][Xpos][1]:#empty space
                    return False
                y +=DirectionY
            return True
        
        else:
            print(Xpos,NewX)
            DirectionX= sign(NewX-Xpos)
            x = Xpos + DirectionX
            print(x) 
            while x !=NewX:
                if chess[Ypos][x][1]:#empty space
                    return False
                x +=DirectionX
            return True
    return False

def KingMove (Ypos,NewY,Xpos,NewX,chess):
    if (NewY != Ypos or NewX != Xpos) and ((NewY <= Ypos + 1 and NewY >= Ypos - 1) and (NewX <=Xpos +1 and NewX >=Xpos - 1)):
        return True
    return False

def PawnMove (Ypos,NewY,Xpos,NewX,chess):
    
    if chess[Ypos][Xpos][1] == "WP":
        if Ypos ==6 and NewY == Ypos - 2 and NewX == Xpos:
            if chess[NewY][NewX][1]:
                return False
            return True
        elif NewY == Ypos - 1 and NewX == Xpos:
            if chess[NewY][NewX][1]:
                return False
            return True
        elif NewY == Ypos - 1 and (NewX == Xpos+1 or NewX == Xpos -1) and chess[NewY][NewX][1] !=0:
            return True
        return False
    

    if chess[Ypos][Xpos][1] == "BP":
        
        if Ypos ==1 and NewY == Ypos + 2 and NewX == Xpos:
            
            if chess[NewY][NewX][1]:
                return False   
            return True
        elif NewY == Ypos + 1 and NewX == Xpos:
        
            if chess[NewY][NewX][1]:
                return False
            return True
        elif NewY == Ypos + 1 and (NewX == Xpos-1 or NewX == Xpos +1) and chess[NewY][NewX][1] != 0:
            return True
        return False
    return False



