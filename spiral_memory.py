# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
import math

# import pdb; pdb.set_trace()
x = 361527

# Start by finding which square x is in.
sq_root_x = math.sqrt(x)
int_sq_root_x = int(sq_root_x)
# Squares sizes are 1, 3, 5, 7, etc.
# If sqrt of x is even, then adding one to it gives us the correct square.
# if sqrt of x is odd and not int then we need to add 2 to get the correct square.
# else sqrt of x is odd int. This is the actual square size.
if int_sq_root_x % 2 == 0:
    square = int_sq_root_x + 1
elif sq_root_x > int_sq_root_x:
    square = int_sq_root_x + 2
else:
    square = int_sq_root_x

# The square starts with ((square-2)^2)+1
square_begins = ((square-2)**2)+1
# The square ends with (square^2)
square_ends = square**2

# find the side x belongs to
if x < (square_begins-1+square-1):  # Right hand side.
    midpoint = square_begins - 1 + int(square/2)
    horizontal_distance = int(square/2)
    vertical_distance = abs(x-midpoint)
elif x < (square_begins-1+(2*(square-1))):    # Top side.
    midpoint = square_begins -1 + (square - 1) + int(square / 2)
    vertical_distance = int(square/2)
    horizontal_distance = abs(x-midpoint)
elif x < (square_begins-1+(3*(square-1))):    # Left side.
    midpoint = square_begins - 1 + (2*(square-1)) + int(square / 2)
    horizontal_distance = int(square/2)
    vertical_distance = abs(x-midpoint)
else:   # Bottom side
    midpoint = square_begins - 1 + (3*(square-1)) + int(square / 2)
    vertical_distance = int(square / 2)
    horizontal_distance = abs(x - midpoint)

distance = vertical_distance + horizontal_distance

print(distance)

