#!/bin/python

import sys

def isOkay(values):
  last_v = values[0]
  for v in values[1:]:
    diff = last_v - v
    last_v = v
    if diff <= 0 or diff > 3:
      return False
  return True

num_reports = 0

fp = sys.argv[1]
with open(fp, 'r') as fh:
  for line in fh.readlines():
    values = [int(v) for v in line.split(' ')]
    if isOkay(values) or isOkay(list(reversed(values))):
      num_reports += 1

print(num_reports)
