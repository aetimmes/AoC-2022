#!/usr/bin/python3.11
"""2017 day 11."""
from collections import Counter

from aocd import get_data, submit

YEAR = 2017
DAY = 11
PART = "a"

# Bug: I had nw and sw swapped in the order leading to misaggregated axial sums.
hex_dirs = [
    "n",
    "ne",
    "se",
    "s",
    "sw",
    "nw",
]


def main():
    """Part a."""
    data = Counter(get_data(day=DAY, year=YEAR).split(","))
    print(f"{data=}")

    axes = [data[dir] for dir in hex_dirs]
    length = len(axes)
    print(f"{axes=}")
    for i in range(length):
        temp = min((axes[j] for j in (i, i - length // 2)))
        axes[i] -= temp
        axes[i - length // 2] -= temp

    print(f"{axes=}")
    right_edge = 0
    for i in range(length):
        if axes[i] and axes[i - 1] and axes[i - 2]:
            right_edge = i

    temp = min(axes[right_edge - i] for i in (0, 2))
    axes[right_edge] -= temp
    axes[right_edge - 1] += temp
    axes[right_edge - 2] -= temp

    result = sum(axes)
    print(f"{axes=}")

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
