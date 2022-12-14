#!/usr/bin/python3.11
"""2017 day 12."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 12
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    connections = {}

    for line in data:
        ls, rs = line.split(" <-> ")
        connections[ls] = rs.split(", ")
    q = ["0"]
    seen = {"0"}
    while q:
        current = q.pop()
        seen.add(current)
        q.extend([c for c in connections[current] if c not in seen])

    result = len(seen)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
