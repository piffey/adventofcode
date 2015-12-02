#!/usr/bin/env python

with open('../inputs/01.txt') as f:
    floor = 0
    line = f.read()
    for i, char in enumerate(line):
        if char == '(': 
            floor += 1
        elif char == ')':
            floor -= 1

        if floor == -1:
            print(i + 1)
            break
