#!/usr/bin/python3

import sys

"""
first column:
    A Rock
    B Paper
    C Scissors
second column:
    X Rock
    Y Paper
    Z Scissors
Convert them to a number (0..2) then calculate success with modulo arithmetic
"""

score = 0

for line in sys.stdin:
    theirs, mine = line.rstrip().split()
    theirs = ord(theirs) - ord('A')
    mine = ord(mine) - ord('X')
    outcome_result = (mine + 4 - theirs) % 3 * 3
    result = outcome_result + (mine + 1)
    score += result
print(f'total score {score}')


