#!/usr/bin/python3.11
"""2017 day 8."""
from collections import defaultdict

from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2017
DAY = 8
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    registers = defaultdict(lambda: 0)

    for line in data:
        ls, rs = (s.split() for s in line.split(" if "))
        condition = f"registers.get('{rs[0]}', 0) {' '.join(rs[1:])}"
        # Bunch of bugs with getting eval syntax to work.
        if eval(condition):  # pylint: disable=eval-used
            if ls[1] == "inc":
                registers[ls[0]] += int(ls[2])
            else:
                registers[ls[0]] -= int(ls[2])

    result = max(registers.values())

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
