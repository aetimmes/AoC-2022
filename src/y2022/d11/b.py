#!/usr/bin/python3.10
"""2022 day 11."""
from aocd import get_data, submit

YEAR = 2022
DAY = 11
PART = "b"


class Monkey:
    """Still a monkey."""

    def __init__(self, items, ops, condition, dests):
        """Initialize."""
        self.items = items
        (self.op1, self.op2) = ops
        self.condition = condition
        (self.tdest, self.fdest) = dests
        self.count = 0


def main():
    """Part b."""
    data = get_data(day=DAY, year=YEAR)
    print(f"{data=}")

    m_data = data.split("\n\n")
    monkeys = []
    for m in m_data:
        lines = m.splitlines()
        lines.pop(0)
        items = [int(x) for x in "".join(lines.pop(0).split()[2:]).split(",")]
        ops = lines.pop(0).split()[-2:]
        condition = int(lines.pop(0).split()[-1])
        dests = (int(lines.pop(0).split()[-1]) for _ in range(2))
        monkeys.append(Monkey(items, ops, condition, dests))

    mod = 1
    for m in monkeys:
        mod *= m.condition

    for _ in range(10000):
        for m in monkeys:
            while m.items:
                m.count += 1
                old = m.items.pop()
                if m.op2 == "old":
                    op2 = old
                else:
                    op2 = int(m.op2)
                if m.op1 == "*":
                    new = old * op2
                else:
                    new = old + op2
                new %= mod
                if new % m.condition == 0:
                    monkeys[m.tdest].items.append(new)
                else:
                    monkeys[m.fdest].items.append(new)

    scores = sorted([m.count for m in monkeys])

    result = scores[-1] * scores[-2]

    print(f"{result=}")
    submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()
