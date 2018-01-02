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


total_valid = 0
with open('input.txt', 'r') as f:
    for line in f:
        passphrase = line.split()
        total_valid += valid(passphrase)

print(total_valid)
