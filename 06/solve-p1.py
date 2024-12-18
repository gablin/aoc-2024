#!/usr/bin/python3

move_chars = '^>v<'
move_map = [ [-1,  0]
           , [ 0, +1]
           , [+1,  0]
           , [ 0, -1]
           ]

with open('input.txt', 'r') as fh:
    mapdata = [l[:-1] for l in fh.readlines()]
max_i = len(mapdata)
max_j = len(mapdata[0])

# Find guard's start position
m = None
p = None
for i in range(max_i):
    line = mapdata[i]
    for j in range(max_j):
        c = line[j]
        if c in move_chars:
            m = move_chars.index(c)
            p = [i, j]
            break
    if p is not None:
        break

def isOnBoard(i, j):
    return i >= 0 and j >= 0 and i < max_i and j < max_j

def mark(i, j):
    mapdata[i] = mapdata[i][:j] + 'X' + mapdata[i][j+1:]

# Move and mark
i = p[0]
j = p[1]
mark(i, j)
while True:
    [di, dj] = move_map[m]

    # Move until guard hits opstacle or moves off the edge
    while ( isOnBoard(i, j) and
            isOnBoard(i+di, j+dj) and
            mapdata[i+di][j+dj] != '#'
          ):
        mark(i, j)
        i += di
        j += dj
    if isOnBoard(i+di, j+dj) and mapdata[i+di][j+dj] == '#':
        m += 1
        if m >= 4:
            m = 0
    else:
        mark(i, j)
        break

# Count 'X'es
result = sum([sum([int(c == 'X') for c in line]) for line in mapdata])
print(result)
