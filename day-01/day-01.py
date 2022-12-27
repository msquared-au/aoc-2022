#!/usr/bin/python3
# day 1

import sys

max_energy = 0
current_energy = 0

"""Echo a message"""
for line in sys.stdin:
    line = line.rstrip()
    if 0 == len(line):
        if current_energy > max_energy:
            max_energy = current_energy
        current_energy = 0
    else:
        current_energy += int(line)
if current_energy > max_energy:
    max_energy = current_energy
print(f'Max energy: {max_energy}')
