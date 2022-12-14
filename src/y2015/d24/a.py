#!/usr/bin/python3.11
"""2015 day 24."""
import math
import sys
from itertools import combinations

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 24
PART = "a"


def can_partition(items, target):
    """Recursively attempt to partition packages."""
    if target == 0:
        return True
    if target < 0:
        return False
    return any(can_partition(items - {item}, target - item) for item in items)


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    packages = {int(line) for line in data}

    target = sum(packages) // 3
    solution, result = None, None

    for i in range(len(data)):
        result = sys.maxsize
        for combo in combinations(packages, i):
            if sum(combo) == target and can_partition(packages - set(combo), target):
                score = math.prod(combo)
                if score < result:
                    result = score
                    solution = combo
        if result != sys.maxsize:
            break

    print(f"{target=}")
    print(f"{solution=}")
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
