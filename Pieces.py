import pygame

class pawn:
    def __init__(self,color):
        self.color = color
        self.image = "Pieces\\Pawn "+color+".png"
class king:
    def __init__(self,color):
        self.color = color
        self.image = "Pieces\\King "+color+".png"
class queen:
    def __init__(self,color):
        self.color = color
        self.image = "Pieces\\Queen "+color+".png"
class bishop:
    def __init__(self,color):
        self.color = color
        self.image = "Pieces\\Bishop "+color+".png"
class knight:
    def __init__(self,color):
        self.color = color
        self.image = "Pieces\\Knight "+color+".png"
class rook:
    def __init__(self,color):
        self.color = color
        self.image = "Pieces\\Rook "+color+".png"
        
