#!/usr/bin/python3.11
"""2017 day 16."""
from aocd import get_data, submit

YEAR = 2017
DAY = 16
PART = "a"


def main():
    """Part a."""
    data = get_data(day=DAY, year=YEAR).split(",")
    print(f"{data=}")

    elements = [chr(ord("a") + i) for i in range(16)]

    for line in data:
        if line[0] == "s":
            elements = [elements[i - int(line[1:])] for i in range(16)]
        if line[0] == "x":
            x, y = map(int, line[1:].split("/"))
            elements[x], elements[y] = elements[y], elements[x]
        if line[0] == "p":
            a, b = line[1:].split("/")
            x, y = elements.index(a), elements.index(b)
            elements[x], elements[y] = elements[y], elements[x]
    result = "".join(elements)
    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
