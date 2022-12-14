#!/usr/bin/python3.11
"""2016 day 20."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 20
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    ranges = [tuple(map(int, line.split("-"))) for line in data]

    result = 0
    for r in sorted(ranges):
        if result < r[0]:
            break
        result = max(r[1] + 1, result)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
