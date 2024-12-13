#!/usr/bin/python3

import re
import sys

with open('input.txt', 'r') as fh:
    data = fh.read()

result = 0
for (x, y) in re.findall(r'mul\(([0-9]+),([0-9]+)\)', data):
    result += int(x) * int(y)
print(result)
