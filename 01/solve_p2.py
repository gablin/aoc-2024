#!/bin/python

import sys

left_values = []
right_values = []

fp = sys.argv[1]
with open(fp, 'r') as fh:
  for line in fh.readlines():
    values = line.split(' ')
    left_values.append(int(values[0]))
    right_values.append(int(values[-1]))

score = 0
for v1 in set(left_values):
  score += v1 * sum([1 for v in right_values if v == v1 ])

print(score)
