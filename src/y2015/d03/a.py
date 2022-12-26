#!/usr/bin/python3.11
"""2015 day 3."""
from aocd import get_data, submit
from numpy import array

YEAR = 2015
DAY = 3
PART = "a"

deltas = {
    "^": array((-1, 0)),
    ">": array((0, 1)),
    "v": array((1, 0)),
    "<": array((0, -1)),
}


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    position = array((0, 0))
    seen = {tuple(position)}

    for c in data:
        position += deltas[c]
        seen.add(tuple(position))

    result = len(seen)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
