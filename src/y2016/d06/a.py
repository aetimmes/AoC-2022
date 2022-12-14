#!/usr/bin/python3.11
"""2016 day 6."""
from collections import Counter

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 6
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = ""

    for i in range(len(data[0])):
        c = Counter("".join(l[i] for l in data))
        result += c.most_common(1)[0][0]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
