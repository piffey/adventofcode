#!/usr/bin/env python

with open('../inputs/02.txt') as f:
    total_ribbon = 0
    for present in f.readlines():
        sides = [int(x) for x in present.split('x')]
        sides.sort()
        ribbon = sides[0] + sides[0] + sides[1] + sides[1]
        bow = sides[0] * sides[1] * sides[2]
        total_ribbon += ribbon + bow
    print(total_ribbon)
