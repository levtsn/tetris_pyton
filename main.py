import pygame




#стакан

def list2d(max,may):
    buf=list()
    for i in range(may):
        buf.append([])
        for j in range(max):
            buf[i].append(i*100+j)
    return buf

FieldMax=10
FieldMay=20

Field=list2d(FieldMax,FieldMay)
print (Field)

#фигура
PieceMax=4
PieceMay=4
Piece=list2d(PieceMax,PieceMay)
PieceX=0
PieceY=0
PieceR=0 #Rotation 0..3

print (Piece)



print (s)
print (s[1][1])
