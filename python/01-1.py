#!/usr/bin/env python

with open('../inputs/01.txt') as f:
    floor = 0
    line = f.read()
    for char in line:
        if char == '(': 
            floor += 1
        elif char == ')':
            floor -= 1
    print(floor)
