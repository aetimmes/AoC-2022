#!/usr/bin/python3.11
"""2015 day 9."""
import itertools
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 13
PART = "a"

DATA = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    m = defaultdict(dict)

    for line in data:
        line = line[:-1]
        t = line.split()
        val = int(t[3]) * (1 if t[2] == "gain" else -1)
        m[t[0]][t[-1]] = val

    for i in itertools.permutations(m.keys()):
        current = 0
        for j in range(len(i)):
            current += m[i[j]][i[j - 1]]
            current += m[i[j - 1]][i[j]]
        result = current if current > result else result

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
