#!/usr/bin/python3.11
"""2017 day 1."""
from aocd import get_data, submit

YEAR = 2017
DAY = 1
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 0
    length = len(data)
    for i in range(length):
        if data[i] == data[(i + 1) % length]:
            result += int(data[i])

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
