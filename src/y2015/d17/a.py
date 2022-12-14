#!/usr/bin/python3.11
"""2015 day 17."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 17
PART = "a"

TARGET = 150


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    sizes_ = tuple(map(int, data))
    counts_ = tuple()
    solutions = set()

    def descent(target, index, sizes, counts):
        """DFS to get sums."""
        if index == len(sizes):
            if target == 0:
                solutions.add(counts)
            return
        for i in [0, 1]:
            descent(target - sizes[index] * i, index + 1, sizes, counts + (i,))

    descent(TARGET, 0, sizes_, counts_)
    result = len(solutions)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
