#!/usr/bin/python3.11
"""2016 day 17."""
import sys
from aocd import get_data, submit
import hashlib

YEAR = 2016
DAY = 17
PART = "a"
VALID = {"b", "c", "d", "e", "f"}
# r, c
DIRS = "UDLR"
DELTAS: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
GRID_SIZE = 4


def bounds_check(r, c, mr, mc):
    return 0 <= r < mr and 0 <= c < mc


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    result = " " * 20000

    state = ((0, 0), "")  # position, path so far
    goal = (3, 3)
    q = [state]

    while q:
        (pos, path) = q.pop()
        if len(path) >= len(result):
            continue
        h = hashlib.md5((data + path).encode("utf-8")).hexdigest()
        for i, d in enumerate(DIRS):
            new_pos = tuple(pos[j] + DELTAS[i][j] for j in [0, 1])
            if h[i] in VALID and bounds_check(
                new_pos[0], new_pos[1], GRID_SIZE, GRID_SIZE
            ):
                if new_pos == goal:
                    if len(result) > len(path):
                        result = path + d
                    continue
                q.append((new_pos, path + d))

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
