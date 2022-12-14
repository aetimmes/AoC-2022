#!/usr/bin/python3.11
"""2016 day 8."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 8
PART = "a"

dimensions = (6, 50)

m = {"row": 0, "column": 1}


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    grid = set()

    for line in data:
        tokens = line.split()
        if tokens[0] == "rect":
            c, r = tuple(map(int, tokens[1].split("x")))
            for i in range(r):
                for j in range(c):
                    grid.add((i, j))
        if tokens[0] == "rotate":
            axis = m[tokens[1]]
            rc_id = int(tokens[2].split("=")[-1])
            n = int(tokens[-1])
            to_move = {x for x in grid if x[axis] == rc_id}
            to_add = set()
            for e in to_move:
                grid.remove(e)
                e = list(e)
                e[axis - 1] = (e[axis - 1] + n) % dimensions[axis - 1]
                to_add.add(tuple(e))
            for e in to_add:
                grid.add(e)

    result = len(grid)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
