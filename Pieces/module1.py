
board=[["R1W","C1W","F1W","K1W","D1W","F2W","C2W","R2W"],
       ["P1W","P2W","P3W","___","P5W","P6W","P7W","P8W"],
       ["___","___","___","___","___","___","___","___"],
       ["___","___","___","___","___","___","___","___"],
       ["___","___","___","___","___","___","___","___"],
       ["___","___","___","___","___","___","___","___"],
       ["P1N","P2N","P3N","P4N","P5N","P6N","P7N","P8N"],
       ["R1N","C1N","F1N","D1N","K1N","F2N","C2N","R2N"]]



def sign(z):
    if z >= 0:
        return 1
    else:
        return -1

def fou_valide(piece,l,m,c,n):
    if piece[0]=="F":#F in french stand for bishop, "Fou",
        if l!=m and  n!=c  and abs(l-m)==abs(c-n): #the condition for the bishop movement
            print("ligma")
            dl = sign(m - l)#it get the me direction of the movement
            dc = sign(n - c)
            x, y = c + dc, l + dl
            print("ligma")
            while x != n and y != m:#This check if they are any non-empty cell on the way
                if board[y][x] != '___': # non empty cell
                    return False
                x += dc
                y += dl
                print(x,y)
            print(x,y)
            return True
        return False
    return True

l = 0
c = 2
m = 2
n = 3
piece = board[l][c] # piece correspond a la piece selectionné

if fou_valide(piece,l,m,c,n)== True:
    board[l][c] = "___"
    board[m][n] = piece
print (board)



print(piece)
