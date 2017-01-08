#!/usr/bin/python

# https://www.hackerrank.com/challenges/botclean

import sys
import heapq
import itertools
from operator import sub
from Queue import PriorityQueue

_dirty = 'd'


def next_move(posr, posc, board):
    pq = PriorityQueue()
    bot = (posc, posr)
    for y, line in enumerate(board):
        for x, c in enumerate(line):
            if c == _dirty:
                dist_v = calc_vertex_distance(bot, (x, y))
                dist = abs(dist_v[0]) + abs(dist_v[1])
                pq.put((dist, dist_v))

    next = pq.get()

    if next[0] == 0:
        print "CLEAN"
    elif abs(next[1][0]) > 0:
        print 'LEFT\n' if next[1][0] > 0 else 'RIGHT\n'
    else:
        print 'UP\n' if next[1][1] > 0 else 'DOWN\n'


def calc_vertex_distance(a, b):
    return tuple(map(sub, a, b))


def main():
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)

if __name__ == "__main__":
    main()

