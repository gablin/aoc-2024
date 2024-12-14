#!/usr/bin/python3

graph_dict = {}
updates = []
with open('input.txt', 'r') as fh:
  in_first_mode = True
  for line in fh.readlines():
    line = line.strip()

    if len(line) == 0:
      in_first_mode = False
      continue

    if in_first_mode:
      [n1, n2] = line.split('|')
      n1 = int(n1)
      n2 = int(n2)
      if n1 in graph_dict:
        graph_dict[n1].add(n2)
      else:
        graph_dict[n1] = set([n2])
    else:
      updates.append([int(n) for n in line.split(',')])

result = 0
for nodes in updates:
  is_okay = True
  while True:
    restart = False
    for (i, n1) in enumerate(nodes):
      for (j, n2) in enumerate(nodes):
        if i == j:
          continue
        if n1 in graph_dict and n2 in graph_dict[n1] and j < i:
          nodes[i] = n2
          nodes[j] = n1
          restart = True
          is_okay = False
          break
      if restart:
        break
    if not restart:
      break
  if not is_okay:
    mid = int(len(nodes) / 2)
    result += nodes[mid]
print(result)
