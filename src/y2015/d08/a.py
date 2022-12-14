#!/usr/bin/python3.11
"""2015 day 8."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 8
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0
    for line in data:
        result += len(line) - len(eval(line))  # pylint: disable=eval-used

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
