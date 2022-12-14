#!/usr/bin/python3.10
"""2022 day 13."""
import json
from itertools import zip_longest

from aocd import get_data, submit

YEAR = 2022
DAY = 13
PART = "a"


def cmp(left, right):
    """Compare two elements, potentially recursively."""
    rc = 0
    if isinstance(left, int):
        if isinstance(right, int):
            rc = right - left
        else:
            rc = cmp([left], right)
    else:
        if isinstance(right, int):
            rc = cmp(left, [right])
        else:
            for (l, r) in zip_longest(left, right, fillvalue=None):
                rc = (l is None) - (r is None)
                if rc == 0:
                    rc = cmp(l, r)
                if rc != 0:
                    break
    return rc


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split("\n\n")
    print(f"{data=}")

    result = 0
    for i, chunk in enumerate(data):
        (left, right) = [json.loads(s) for s in chunk.split("\n")]
        return_code = cmp(left, right)
        if return_code > 0:
            result += i + 1
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
