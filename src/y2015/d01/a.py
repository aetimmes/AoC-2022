#!/usr/bin/python3.11
"""2015 day 1."""
from aocd import get_data, submit

YEAR = 2015
DAY = 1  # FIX ME
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 0
    for c in data:
        if c == "(":
            result += 1
        elif c == ")":
            result -= 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
