#!/bin/python
from operator import sub

# https://www.hackerrank.com/challenges/saveprincess

_bot = 'm'
_princess = 'p'

def displayPathtoPrincess(n, grid):
    bot_loc = (None, None)
    princess_loc = (None, None)
    for lineIdx, line in enumerate(grid):
        for cIdx, c in enumerate(line):
            if c == _bot: bot_loc = (cIdx, lineIdx)
            elif c == _princess: princess_loc = (cIdx, lineIdx)
    distance = tuple(map(sub, bot_loc, princess_loc))

    output = ('UP\n' if distance[1] > 0 else 'DOWN\n') * abs(distance[1])
    output += ('LEFT\n' if distance[0] > 0 else 'RIGHT\n') * abs(distance[0])
    output = output.rstrip()
    print(output)

def main():
    m = input()

    grid = []
    for i in xrange(0, m):
        grid.append(raw_input().strip())

    displayPathtoPrincess(m,grid)

if __name__ == '__main__':
    main()