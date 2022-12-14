#!/usr/bin/python3.11
"""2017 day 9."""
from aocd import get_data, submit

YEAR = 2017
DAY = 9
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = 0
    depth = 0
    garbage = False
    i = 0
    while i < len(data):
        c = data[i]
        if garbage:
            if c == ">":
                garbage = False
            if c == "!":
                i += 1
        elif c == "<":
            garbage = True
        elif c == "{":
            depth += 1
        elif c == "}":
            result += depth
            depth -= 1
        i += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
