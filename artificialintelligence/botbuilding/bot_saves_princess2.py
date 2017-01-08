#!/bin/python
from operator import sub

# https://www.hackerrank.com/challenges/saveprincess2

_bot = 'm'
_princess = 'p'

def nextMove(n,r,c,grid):
    bot_loc = (c, r)
    princess_loc = (None, None)
    for lineIdx, line in enumerate(grid):
        for cIdx, c in enumerate(line):
            if c == _princess:
                princess_loc = (cIdx, lineIdx)
    distance = tuple(map(sub, bot_loc, princess_loc))
    output = ''
    if distance[1] != 0:
        output = 'UP\n' if distance[1] > 0 else 'DOWN\n'
    if len(output) == 0 and distance[0] != 0:
        output = ('LEFT\n' if distance[0] > 0 else 'RIGHT\n')
    return output

def main():
    n = input()
    r, c = [int(i) for i in raw_input().strip().split()]
    grid = []
    for i in xrange(0, n):
        grid.append(raw_input())

    print nextMove(n, r, c, grid)

if __name__ == '__main__':
    main()