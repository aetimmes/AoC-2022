#!/usr/bin/python3.11
"""2015 day 6."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2015
DAY = 6
PART = "a"


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    grid = set()

    for line in data:
        tokens = line.split()
        if tokens[0] == "toggle":
            x1, y1 = (int(t) for t in tokens[1].split(","))
            x2, y2 = (int(t) for t in tokens[3].split(","))
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in grid:
                        grid.remove((x, y))
                    else:
                        grid.add((x, y))
        elif tokens[1] == "on":
            x1, y1 = (int(t) for t in tokens[2].split(","))
            x2, y2 = (int(t) for t in tokens[4].split(","))
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid.add((x, y))
        elif tokens[1] == "off":
            x1, y1 = (int(t) for t in tokens[2].split(","))
            x2, y2 = (int(t) for t in tokens[4].split(","))
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid.discard((x, y))
    result = len(grid)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
