#!/usr/bin/env python

with open('../inputs/03.txt') as f:
    santas_coords = [0, 0]
    neighborhood_map = {}

    for move in f.readline():
        if move == '>':
            santas_coords[1] += 1
        elif move == '<':
            santas_coords[1] -= 1
        elif move == '^':
            santas_coords[0] += 1
        elif move == 'v':
            santas_coords[0] -= 1

        key_coords = ','.join([str(x) for x in santas_coords])
        if neighborhood_map.get(key_coords):
            neighborhood_map[key_coords] += 1
        else:
            neighborhood_map[key_coords] = 1

    print(len(neighborhood_map.keys()))
