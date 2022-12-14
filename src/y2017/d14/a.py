#!/usr/bin/python3.11
"""2017 day 14."""
from collections import Counter
from aocd import get_data, submit

YEAR = 2017
DAY = 14
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")
    grid = []
    for i in range(128):
        grid.append(get_knot_hash(f"{data}-{i}"))

    result = 0
    for line in grid:
        for e in line:
            result += Counter(f"{e:08b}")["1"]
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


def get_knot_hash(input_string):
    """Get the knot hash of an input string."""
    lengths = [ord(c) for c in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    elements = list(range(256))
    current = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            if length > len(elements):
                continue
            temp = elements + elements
            temp = (
                temp[0:current]
                + list(reversed(temp[current:current + length]))
                + temp[current + length:]
            )
            elements = (
                temp[(len(temp) // 2):len(temp) // 2 + current]
                + temp[current:len(temp) // 2]
            )
            current += length + skip
            current %= len(elements)
            skip += 1

    result = get_dense_hash(elements)
    return result


def get_dense_hash(elements):
    """Get the hex hash of a list of elements."""
    result = []
    for i in range(16):
        chars = elements[i * 16:(i + 1) * 16]
        e = chars[0]
        for c in chars[1:]:
            e ^= c
        result.append(e)
    return result


if __name__ == "__main__":
    main()
