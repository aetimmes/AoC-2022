#!/usr/bin/python3.11
"""2015 day 20."""
import math

from aocd import get_data, submit

YEAR = 2015
DAY = 20
PART = "a"


def calc_house(n):
    """Determine how many presents house n gets."""
    result = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            result += 10 * i
            j = n // i
            if j != i:
                result += 10 * j
    return result


def main():
    """Part a."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 1

    while calc_house(result) < data:
        result += 1
        if result % 10000 == 0:
            print(result, calc_house(result))

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
