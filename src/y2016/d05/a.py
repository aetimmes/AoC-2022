#!/usr/bin/python3.11
"""2016 day 5."""
import hashlib

from aocd import get_data, submit

YEAR = 2016
DAY = 5
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = ""
    index = 0

    while len(result) < 8:
        h = hashlib.md5((data + str(index)).encode("utf-8")).hexdigest()
        if h[:5] == "00000":
            result += h[5]
        index += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
