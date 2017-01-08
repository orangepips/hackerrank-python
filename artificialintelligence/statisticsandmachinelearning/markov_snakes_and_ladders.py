# import numpy as np
from random import random
from bisect import bisect

# https://www.hackerrank.com/challenges/markov-snakes-and-ladders

simulations_per_test = 2500
start = 1
end = 100
max_moves = 1000


def get_cum_weights(probabilities):
    total = 0
    cum_weights = []
    for p in probabilities:
        total += p
        cum_weights.append(total)
    return cum_weights


def get_die_rolls(probabilities, cum_weights):
    # http: // stackoverflow.com / questions / 3679694 / a - weighted - version - of - random - choice
    # return np.random.choice(6, max_moves, p=probabilities)

    # print(probabilities)
    # print(cum_weights)
    values = [0, 1, 2, 3, 4, 5]

    rolls = []
    for i in xrange(0, max_moves):
        x = random()
        i = bisect(cum_weights, x)
        rolls.append(values[i])
    # print(rolls)
    return rolls


def play(test):
    snakes_and_ladders = dict(test['snakes'].items() + test['ladders'].items())
    transition_matrix = []
    for x in xrange(1, 100):
        row = {}
        for i in xrange(1, 7):
            if i + x > 100: row[i] = x
            elif i+x in snakes_and_ladders:
                row[i] = snakes_and_ladders[i+x]
            else: row[i] = i + x
        transition_matrix.append(row)

    # print(transition_matrix)
    simulation_move_counts = []

    probabilities = test['probabilities']
    cum_weights = get_cum_weights(probabilities)
    while len(simulation_move_counts) < simulations_per_test:
        rolls = get_die_rolls(probabilities, cum_weights)
        # print(rolls)
        current = start
        for moves, roll in enumerate(rolls):
            roll += 1
            # print("Moves: {} Current: {} Roll: {}".format(moves + 1, current, roll))
            # print(current, roll)
            current = transition_matrix[current - 1][roll]
            if moves >= max_moves or current >= end:
                simulation_move_counts.append(moves + 1)
                break

    return sum(simulation_move_counts) / float(simulations_per_test)


def tuples2dict(line):
    return dict([tuple([int(x) for x in x.split(',')]) for x in line.split()])


def main():
    n = input()
    tests = []
    for i in xrange(0, n):
        test = {}
        test['probabilities'] = [float(x) for x in raw_input().split(',')]
        raw_input() # snake and ladder count
        # test.ladder_count, test.snake_count = [int(x) for x in raw_input().split(',')]
        test['ladders'] = tuples2dict(raw_input())
        test['snakes'] = tuples2dict(raw_input())
        tests.append(test)
    for test in tests:
        print(play(test))

if __name__ == '__main__':
    main()