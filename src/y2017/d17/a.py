#!/usr/bin/python3.11
"""2017 day 17."""
from aocd import get_data, submit

YEAR = 2017
DAY = 17
PART = "a"


def main():
    """Part a."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    elements = [0]
    pos = 0
    for i in range(2017):
        pos += data
        pos %= len(elements)
        elements.insert(pos + 1, i + 1)
        pos += 1

    result = elements[pos + 1]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
