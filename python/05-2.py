#!/usr/bin/env python

import re

def nice_string(string):
    string = string.strip()
    has_between = False
    has_repeat = False

    for pos, letter in enumerate(string):
        if re.search(r'{}[a-z]{}'.format(letter, letter, letter), string):
            has_between = True

        # Add something we know won't repeat so we don't have to check if we're at the end of the line.
        stringb = string + "0"
        double = r'{}{}'.format(letter, stringb[pos + 1])
        if len(re.findall(double, string)) >= 2:
            # Check splits to make sure we don't have any overlaps. This is cheating.
            if len(re.split(double, string)) - 1 == len(re.findall(double, string)):
                has_repeat = True

    if has_between and has_repeat:
        return True

    return False

nice_strings = 0
with open('../inputs/05.txt') as f:
    for string in f:
        if nice_string(string):
            nice_strings += 1

print(nice_strings)
