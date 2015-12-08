#!/usr/bin/env python

def nice_string(string):
    number_of_vowels = 0
    last_letter = None
    double_letter = False
    three_vowels = False
    has_disallowed_string = False

    for letter in string:
        if letter == last_letter:
            double_letter = True

        if letter in ['a', 'e', 'i', 'o', 'u']:
            number_of_vowels += 1
            if number_of_vowels >= 3:
                three_vowels = True

        if '{}{}'.format(last_letter, letter) in ['ab', 'cd', 'pq', 'xy']:
            has_disallowed_string = True

        last_letter = letter

    if double_letter and three_vowels and not has_disallowed_string:
        return True

    return False

nice_strings = 0
with open('../inputs/05.txt') as f:
    for string in f:
        if nice_string(string):
            nice_strings += 1

print(nice_strings)
