# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals


def valid(pp):
    """Check that the pp list has no repeated items

        input: pp is a list of strings.
        returns 0 if a repeat is found, 1 otherwise"""
    while pp:
        w = pp.pop(0)
        if w in pp:
            return 0
    return 1


def sort_string(x):
    return ''.join(sorted(x))


total_valid = 0
with open('input.txt', 'r') as f:
    for line in f:
        passphrase = line.split()
        # Sort the strings in the list then check there are no repeats.
        total_valid += valid(list(map(sort_string, passphrase)))

print(total_valid)
