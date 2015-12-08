#!/usr/bin/env python

with open('../inputs/03.txt') as f:
    santas_coords = [0, 0]
    robo_santas_coords = [0, 0]
    neighborhood_map = {}
    santas_turn = True

    for move in f.readline():
        if move == '>':
            if santas_turn:
                santas_coords[1] += 1
            else:
                robo_santas_coords[1] += 1
        elif move == '<':
            if santas_turn:
                santas_coords[1] -= 1
            else:
                robo_santas_coords[1] -= 1
        elif move == '^':
            if santas_turn:
                santas_coords[0] += 1
            else:
                robo_santas_coords[0] += 1
        elif move == 'v':
            if santas_turn:
                santas_coords[0] -= 1
            else:
                robo_santas_coords[0] -= 1

        if santas_turn:
            key_coords = ','.join([str(x) for x in santas_coords])
        else:
            key_coords = ','.join([str(x) for x in robo_santas_coords])

        if neighborhood_map.get(key_coords):
            neighborhood_map[key_coords] += 1
        else:
            neighborhood_map[key_coords] = 1

        santas_turn = not santas_turn

    print(len(neighborhood_map.keys()))
