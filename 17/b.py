#!/usr/bin/python3.10
"""2022 day 17."""
from aocd import get_data, submit
from aocd.transforms import lines

YEAR = 2022
DAY = 17
PART = "b"

# bottom left is (0,0)
# grow bottom -> up, left -> right

flat = ((0, 0), (0, 1), (0, 2), (0, 3))
plus = ((1, 0), (1, 1), (0, 1), (2, 1), (1, 2))
el = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2))
eye = ((0, 0), (1, 0), (2, 0), (3, 0))
square = ((0, 0), (1, 0), (0, 1), (1, 1))

pieces = [flat, plus, el, eye, square]

num_pieces = len(pieces)

delta = {"<": -1, ">": 1}

num_steps = 1000000000000

DATA = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"


def main():
    """Part b."""
    # data = get_data(day=DAY, year=YEAR)
    data = DATA
    print(f"{data=}")

    data_len = len(data)

    rocks = set()

    def bounds_check(r, c):
        return r >= 0 and c >= 0 and c < 7 and (r, c) not in rocks

    t = 0

    max_heights = [-1]

    end_state_map = {}

    for i in range(num_steps):
        if i > 0 and i % num_pieces == 0 and t % data_len == 0:
            break
        current_piece = [
            [r + max_heights[-1] + 4, c + 2] for r, c in pieces[i % num_pieces]
        ]
        delta_sum = 0
        cycle_found = False
        while not cycle_found:
            d = delta[data[t % data_len]]
            delta_sum += d
            if all(bounds_check(r, c + d) for r, c in current_piece):
                for rock in current_piece:
                    rock[1] += d
            t += 1
            if all(bounds_check(r - 1, c) for r, c in current_piece):
                current_piece = [[r - 1, c] for (r, c) in current_piece]
            else:
                for (r, c) in current_piece:
                    rocks.add((r, c))
                max_heights.append(
                    max([max_heights[-1]] + [r for r, _ in current_piece])
                )
                x = (i % num_pieces, t % data_len, delta_sum)
                if x in end_state_map:
                    cycle_start, cycle_end = end_state_map[x][0], i
                    cycle_height = max_heights[-1] - end_state_map[x][1]
                    cycle_found = True
                else:
                    end_state_map[x] = (i, max_heights[-1])
                break

    cycle_length = cycle_end - cycle_start

    num_cycles = (num_steps - cycle_end) // cycle_length

    result += max_heights[leftover_cycles + 1]

    print(f"{result=}")
    # submit(result, part=PART, day=DAY, year=YEAR)


if __name__ == "__main__":
    main()