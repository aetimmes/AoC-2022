#!/usr/bin/python3.11
"""2016 day 19."""
from aocd import get_data, submit

YEAR = 2016
DAY = 19
PART = "a"


def main():
    """Part a."""
    data = int(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    elves = set(range(data))

    purge = False
    while len(elves) > 1:
        elf_list = sorted(elves)
        for e in elf_list:
            if purge:
                elves.remove(e)
            purge = not purge

    result = elves.pop() + 1
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
