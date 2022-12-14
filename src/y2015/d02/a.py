#!/usr/bin/python3.11
"""2015 day 2."""
import sys
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 2
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        tokens = [int(x) for x in line.split("x")]
        min_ = sys.maxsize
        for i in range(len(tokens)):
            side = tokens[i] * tokens[i - 1]
            result += 2*side
            if side < min_:
                min_ = side
        result += min_

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
