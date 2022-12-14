#!/usr/bin/python3.11
"""2016 day 7."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2016
DAY = 7
PART = "a"


def supports_tls(line):
    """Check an IP to see if it supports TLS."""
    outies = []
    innies = []
    while "[" in line:
        ls, line = line.split("[", 1)
        outies.append(ls)
        mid, line = line.split("]", 1)
        innies.append(mid)
    if line:
        outies.append(line)
    return (not any(has_abba(i) for i in innies)) and any(has_abba(o) for o in outies)


def has_abba(s):
    """Check a string to see if it contains an ABBA."""
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def main():
    """Part a."""
    data = lines(get_data(day=DAY, year=YEAR))
    print(f"{data=}")

    result = 0

    for line in data:
        if supports_tls(line):
            result += 1

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
