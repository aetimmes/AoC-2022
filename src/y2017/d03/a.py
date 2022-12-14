#!/usr/bin/python3.11
"""2017 day 3."""
import math
from aocd import get_data, submit

YEAR = 2017
DAY = 3
PART = "a"

# r,c
deltas = ((0, 1), (-1, 0), (0, -1), (1, 0))


def nth_side_len(n):
    return math.ceil(n / 2)


def main():
    """Part a."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    (r, c) = (0, 0)
    direction = 0
    side = 1
    current = 1
    # Off-by-one error:
    # for _ in range(0, data):
    # We don't need to do a move for the first number.
    for _ in range(1, data):
        r += deltas[direction][0]
        # Copy-paste error:
        # r += deltas[direction][1]
        # Should be modifying c there.
        c += deltas[direction][1]
        # Logic error:
        # result += abs(r) + abs(c)
        # We only need the MH distance of the end point, not the sum of every point.
        current -= 1
        if current == 0:
            side += 1
            direction += 1
            direction %= 4
            current = nth_side_len(side)

    result = abs(r) + abs(c)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
