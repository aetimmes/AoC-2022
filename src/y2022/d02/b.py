#!/usr/bin/python3.10
"""2022 day 2."""
from aocd import get_data, submit

YEAR = 2022
DAY = 2
PART = "b"

SCORES = [1, 2, 3]
RESULTS = [0, 3, 6]


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR).split("\n")
    print(f"{data=}")

    result = 0
    for line in data:
        tokens = line.split()
        i_a = ord(tokens[0]) - ord("A")
        i_b = ord(tokens[1]) - ord("X")
        result += RESULTS[i_b]
        result += SCORES[(i_a + i_b - 1) % 3]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
