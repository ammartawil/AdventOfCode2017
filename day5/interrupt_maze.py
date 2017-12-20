# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

with open('input.txt', 'r') as f:
    jumps = f.read().strip().split()

current_position = 0
# jump = int(jumps[current_position])
total_jumps = 0

while current_position < len(jumps):
    jump = int(jumps[current_position])
    next_position = current_position + jump
    jumps[current_position] = jump + 1
    current_position = next_position
    total_jumps += 1

print(total_jumps)

