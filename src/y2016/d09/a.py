#!/usr/bin/python3.11
"""2016 day 9."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 9
PART = "a"


def main():
    """Part a."""
    data = "".join(lines(get_data(day=DAY, year=YEAR)))
    print(f"{data=}")

    decompressed = ""

    while "(" in data:
        ls, data = data.split("(", 1)
        decompressed += ls
        mid, data = data.split(")", 1)
        char_count, copy_count = tuple(map(int, mid.split("x")))

        repeated, data = data[:char_count], data[char_count:]
        decompressed += repeated * copy_count

    if data:
        decompressed += data

    result = len(decompressed)

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
