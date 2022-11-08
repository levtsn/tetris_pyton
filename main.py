# import pygame


# стакан

def create_list2d(max, may, value=0):
    buf = list()
    for i in range(may):
        buf.append([])
        for j in range(max):
            buf[i].append(value)
    return buf


field_max = 5
field_may = 6

field = create_list2d(field_max, field_may)
print(field)

# фигура
piece_max = 4
piece_may = 4

piece_x = 0
piece_y = 0
piece_r = 0  # Rotation 0..3

# Piece = list2d(PieceMax, PieceMay)
piece = create_list2d(piece_max, piece_may)
print(piece)


def check_collision():
    for x in range(piece_max):
        for y in range(piece_may):
            cx = x + piece_x
            cy = y + piece_y
            if cx in range(field_max) and cy in range(field_may):
                if piece[x][y] != 0 and field[cx][cy] != 0:
                    return True
    return False


def field_remove_full_lines():
    for y in range(len(field)):
        full=True
        for x in range(len(field[y])):
            if field[y][x] == 0:
                full=False
        if full==True:

            for y2 in range(y, 1, -1):
                field[y2] = field[y2 - 1]

            for i in range(len(field[0])):
                field[0][i] = 0


piece_x = 0
piece_y = 0
print(check_collision())

field = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0]
#
]

print(field)
field_remove_full_lines()
print ("after")
print(field)

print()
