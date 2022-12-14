#!/usr/bin/python3.11
"""2016 day 13."""
from collections import Counter
from aocd import get_data, submit
from aocd.transforms import lines
from numpy import array

YEAR = 2016
DAY = 13
PART = "a"


deltas = (array((1, 0)), array((0, 1)), array((-1, 0)), array((0, -1)))


def bounds_check(candidate, i: int):
    (r, c) = candidate
    return (
        r >= 0
        and c >= 0
        and Counter(str(bin(c * c + 3 * c + 2 * c * r + r + r * r + i))[2:])["1"] % 2
        == 0
    )


def main():
    """Part a."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    current = array((1, 1))
    goal = (39, 31)
    seen = set()
    q = [current]
    done = False
    while not done:
        result += 1
        next_ = []
        while q and not done:
            current = q.pop()
            seen.add(tuple(current))
            for d in deltas:
                candidate = current + d
                if tuple(candidate) == goal:
                    done = True
                    break
                if tuple(candidate) not in seen and bounds_check(candidate, data):
                    next_.append(candidate)
        q = next_

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
