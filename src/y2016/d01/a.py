#!/usr/bin/python3.11
"""2016 day 1."""
from aocd import get_data, submit
from numpy import array

YEAR = 2016
DAY = 1
PART = "a"

deltas = [array([-1, 0]), array([0, 1]), array([1, 0]), array([0, -1])]

turns = {"L": -1, "R": 1}


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split(", ")
    print(f"{data=}")

    position = array([0, 0])
    facing = 0

    for token in data:
        facing += turns[token[0]]
        facing %= 4
        position += deltas[facing] * int(token[1:])

    result = sum(abs(position))

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
