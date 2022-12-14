#!/usr/bin/python3.11
"""2017 day 15."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 15
PART = "a"

A = 16807
B = 48271
DIVISOR = 2147483647


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    a, b = (int(line.split()[-1]) for line in data)

    result = 0
    for _ in range(40_000_000):
        a *= A
        b *= B
        a %= DIVISOR
        b %= DIVISOR
        if f"{a:016b}"[-16:] == f"{b:016b}"[-16:]:
            result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
