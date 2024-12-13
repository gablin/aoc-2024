#!/usr/bin/python3

import re
import sys

with open('input.txt', 'r') as fh:
    data = fh.read()

is_enabled = True
result = 0
for (x, y, do, dont) in re.findall(r'mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don\'t\(\))', data):
    if x and y and is_enabled:
        result += int(x) * int(y)
    elif do:
        is_enabled = True
    elif dont:
        is_enabled = False
print(result)
