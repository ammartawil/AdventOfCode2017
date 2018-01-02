# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


def calc_new_value(x,y):
    # Calculates the value of position spiral[x][y] by adding all the cells around it.
    value=0
    for xcell in range(offset+x-1, offset+x+2):
        for ycell in range(offset+y-1, offset+y+2):
            value += spiral[xcell][ycell]
    return value

def get_cell_value(x,y):
    return spiral[x+offset][y+offset]

def set_cell_value(x,y,v):
    spiral[x+offset][y+offset] = v


# Build a list of lists to hold the spiral
spiral = []
spiral_size = 11
row = []
for i in range(0, spiral_size):
    row.append(0)

for column in range(0,spiral_size):
    spiral.append([0]*spiral_size)

offset = int(spiral_size/2)
spiral[offset][offset]=1

# Build the spiral
steps = 2
current_x = 0
current_y = 0

while get_cell_value(current_x,current_y) <= 361527:
    # move current x,y one cell right to start a new spiral
    current_x += 1
    # go steps up
    for i in range(current_y, current_y + steps):
        set_cell_value(current_x,i,calc_new_value(current_x,i))
    current_y = i
    current_x -= 1
    # go steps left
    for i in range(current_x, current_x - steps,-1):
        set_cell_value(i, current_y, calc_new_value(i, current_y))
    current_x = i
    current_y -= 1
    # go steps down
    for i in range(current_y, current_y - steps,-1):
        set_cell_value(current_x, i, calc_new_value(current_x, i))
    current_y = i
    current_x += 1
    # go steps right
    for i in range(current_x, current_x + steps):
        set_cell_value(i, current_y, calc_new_value(i, current_y))
    current_x = i

    steps += 2

for row in spiral:
    for n in row:
        print('{0:07}'.format(n), end='  ')
    print('\n')

# Answer = 363010
