#!/usr/bin/python3

move_chars = '^>v<'
move_map = [ [-1,  0]
           , [ 0, +1]
           , [+1,  0]
           , [ 0, -1]
           ]

with open('input.txt', 'r') as fh:
    orig_mapdata = [l[:-1] for l in fh.readlines()]
max_i = len(orig_mapdata)
max_j = len(orig_mapdata[0])

num_positions = 0
prev_num = 0
for x in range(max_i):
    for y in range(max_j):
        if num_positions != prev_num:
            print(num_positions)
        prev_num = num_positions

        # Skip positions where there's already an obstacle or where the guard
        # starts
        c = orig_mapdata[x][y]
        if c == '#' or c in move_chars:
            continue

        mapdata = [line for line in orig_mapdata]
        mapdata[x] = mapdata[x][:y] + '#' + mapdata[x][y+1:]

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

        # Remember visited positions together with current direction (if we see
        # this again, we know the guard is stuck in a loop)
        visit_set = set()

        def visit(i, j, m):
            visit_set.add((i, j, m))

        def hasAlreadyVisited(i, j, m):
            return (i, j, m) in visit_set

        # Move and mark
        is_stuck = False
        i = p[0]
        j = p[1]
        while True:
            if hasAlreadyVisited(i, j, m):
                is_stuck = True
                break
            visit(i, j, m)

            [di, dj] = move_map[m]

            # Move until guard hits opstacle or moves off the edge
            while ( isOnBoard(i, j) and
                    isOnBoard(i+di, j+dj) and
                    mapdata[i+di][j+dj] != '#'
                  ):
                i += di
                j += dj
            if isOnBoard(i+di, j+dj) and mapdata[i+di][j+dj] == '#':
                m += 1
                if m >= 4:
                    m = 0
            else:
                break
        if is_stuck:
            num_positions += 1
print('Done')
