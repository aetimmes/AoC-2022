#!/usr/bin/python3.11
"""2017 day 5."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 5
PART = "a"


def main():
    """Part a."""
    data = [int(line) for line in lines(get_data(day=DAY, year=YEAR))]
    print(f"{data=}")

    result = 0
    ic = 0
    while 0 <= ic < len(data):
        result += 1
        next_ = ic + data[ic]
        # Reading comprehension bug: Originally, I thought negative jump values were
        # decremented and positive values were incremented. For some reason, I thought
        # the zero case was treated like an increment, which caused another (invalid)
        # divide-by-zero bug because I didn't account for the case where data[ic] == 0.
        data[ic] += 1
        ic = next_
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
