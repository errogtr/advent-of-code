import click
from aoc.utils import read_data, timer


def nn(x, y):
    return [
        (x, y - 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x, y + 1),
        (x - 1, y + 1),
        (x - 1, y),
        (x - 1, y - 1),
    ]



def visible(x, y, seats):
    def _scan_row(row):
        for el in row:
            if el != ".":
                yield el

    visible_seat = next(_scan_row(seats[y][x+1:]), ".")
    return visible_seat
    

def rotate(seats):
    return list(zip(*seats[::-1]))


def single_round_adj(state):
    next_state = dict()
    for (x, y), v in state.items():
        if v == "L" and all(state.get((w, z), ".") != "#" for w, z in nn(x, y)):
            next_state[(x, y)] = "#"
        elif v == "#" and sum(state.get((w, z), ".") == "#" for w, z in nn(x, y)) >= 4:
            next_state[(x, y)] = "L"
        else:
            next_state[(x, y)] = state[(x, y)]
    return next_state


def single_round_vis(state):
    next_state = list()
    for y, row in enumerate(state):
        for x, seat in enumerate(row):
            if seat == ".":
                continue
            visible_seats = list()  
            visible_seats_right = visible(x, y, state)
            visible_seats_left = visible(x, y, rotate(rotate(state)))
            visible_seats_up = visible(x, y, rotate(rotate(rotate(state))))
            visible_seats_down = visible(x, y, rotate(state))
            visible_seats_up_right = ...
            visible_seats_up_left = ...
            visible_seats_down_right = ...
            visible_seats_down_left = ...

        # if v == "L" and all(state.get((w, z), ".") != "#" for w, z in nn(x, y)):
        #     next_state[(x, y)] = "#"
        # elif v == "#" and sum(state.get((w, z), ".") == "#" for w, z in nn(x, y)) >= 4:
        #     next_state[(x, y)] = "L"
        # else:
        #     next_state[(x, y)] = state[(x, y)]
    # return next_state


@timer
def part1(start):
    while True:
        end = single_round_adj(start)
        if end == start:
            break
        start = end
    return sum(v == "#" for v in end.values())


@timer
def part2(start):
    while True:
        end = single_round_vis(start)
        if end == start:
            break
        start = end
    return sum(v == "#" for v in end.values())


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    seats = {
        (x, y): v
        for y, row in enumerate(data.splitlines())
        for x, v in enumerate(row)
    }

    # ==== PART 1 ====
    print(part1(seats))

    # ==== PART 2 ====
    print(part2(data.splitlines()))


if __name__ == "__main__":
    main()
