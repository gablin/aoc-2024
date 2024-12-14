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

left_values.sort()
right_values.sort()

dists = 0
for (x, y) in zip(left_values, right_values):
  dists += abs(x - y)

print(dists)
