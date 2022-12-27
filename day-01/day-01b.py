#!/usr/bin/python3
# day 1

import sys

energy = []
current_energy = 0

for line in sys.stdin:
    line = line.rstrip()
    if 0 == len(line):
        energy.append(current_energy)
        current_energy = 0
    else:
        current_energy += int(line)
if current_energy > 0:
    energy.append(current_energy)
energy.sort(reverse=True)
print(f'Max energy: {sum(energy[:3])}')
