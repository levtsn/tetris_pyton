import pygame


# стакан

def list2d(max, may, value=0):
    buf = list()
    for i in range(may):
        buf.append([])
        for j in range(max):
            buf[i].append(value)
    return buf


FieldMax = 10
FieldMay = 20

Field = list2d(FieldMax, FieldMay)
print(Field)

# фигура
PieceMax = 4
PieceMay = 4

PieceX = 0
PieceY = 0
PieceR = 0  # Rotation 0..3

#Piece = list2d(PieceMax, PieceMay)
Piece = list2d(PieceMax, PieceMay)
print(Piece)

def CollisionCheck():
    for x in range(PieceMax):
        for y in range(PieceMay):
            cx=x+PieceX
            cy=y+PieceY
            if cx in range(FieldMax) and cy in range (FieldMay):
                if Piece[x][y]!=0 and Field[cx][cy]!=0:
                    return True
    return False
PieceX=0
PieceY=0
print (CollisionCheck())
