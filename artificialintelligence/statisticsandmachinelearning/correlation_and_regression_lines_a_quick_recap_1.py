import math

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_def(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)

# Physics Scores  15  12  8   8   7   7   7   6   5   3
# History Scores  10  25  17  11  13  17  20  13  9   15

def main():
    a = [int(x) for x in ("15  12  8   8   7   7   7   6   5   3".split())]
    b = [int (x) for x in "10  25  17  11  13  17  20  13  9   15".split()]
    print pearson_def(a, b)

if __name__ == '__main__':
    main()