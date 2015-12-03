#!/usr/bin/env python

with open('../inputs/02.txt') as f:
    total_wrapping_paper = 0
    for present in f.readlines():
        l, w, h = [int(x) for x in present.split('x')]
        sides = [l * w, l * h, h * w]
        sides.sort()
        surface_area = sides[0]
        sides = [2 * x for x in sides]
        surface_area += sum(sides)
        total_wrapping_paper += surface_area
    print(total_wrapping_paper)
