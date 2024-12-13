#!/usr/bin/python3

import sys

with open('input.txt', 'r') as fh:
    lines = [l[:-1] for l in fh.readlines()]

def checkWord(word, i, j, di, dj):
    global lines

    try:
        for k in range(len(word)):
            if i < 0 or j < 0:
                return False

            if lines[i][j] != word[k]:
                return False
            i += di
            j += dj
        return True
    except Exception as e:
        return False

def countWords(word, i, j):
    return ( int(checkWord(word, i, j,  0, +1)) +
             int(checkWord(word, i, j, +1, +1)) +
             int(checkWord(word, i, j, +1,  0)) +
             int(checkWord(word, i, j, +1, -1)) +
             int(checkWord(word, i, j,  0, -1)) +
             int(checkWord(word, i, j, -1, -1)) +
             int(checkWord(word, i, j, -1,  0)) +
             int(checkWord(word, i, j, -1, +1))
           )

result = 0
for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        result += countWords('XMAS', i, j)
print(result)
