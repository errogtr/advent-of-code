from copy import copy
import click
from aoc.utils import read_data, timer

# fmt: off
# Turn rules
TURNS = {
    ("/", 1): -1j, ("/", -1): 1j, ("/", 1j): -1, ("/", -1j): 1,
    ("\\", 1): 1j, ("\\", -1): -1j, ("\\", 1j): 1, ("\\", -1j): -1,
}

# Crossing rules
L, S, R = "L", "S", "R"
CROSSINGS = {
    (L, 1): -1j, (L, -1): 1j, (L, 1j): 1, (L, -1j): -1,
    (S, 1): 1, (S, -1): -1, (S, 1j): 1j, (S, -1j): -1j,
    (R , 1): 1j, (R , -1): -1j, (R   , 1j): -1, (R  , -1j): 1,
}
ROTATIONS = {L: S, S: R, R : L}
# fmt: on


def parse(data):
    # Assumption: carts never starts on turns ('/', '\') or crossings ('+'). This is
    #             true for my input, but I can't be sure the same holds for everyone
    overlaps = {"^": "|", "v": "|", ">": "-", "<": "-"}
    dirs = {">": 1, "<": -1, "^": -1j, "v": 1j}

    track, carts = {}, []
    for y, line in enumerate(data.splitlines()):
        for x, val in enumerate(line):
            z = x + 1j * y
            if val in ("\\", "/", "-", "|", "+"):
                track[z] = val
            elif val != " ":
                carts.append((z, dirs[val], L))
                track[z] = overlaps[val]
    return track, carts


def tick(track, carts, remove_crashed=True):
    carts = sorted(carts, key=lambda cart: (cart[0].imag, cart[0].real))
    next_carts = copy(carts)

    occupied = {pos: i for i, (pos, _, _) in enumerate(carts)}
    crashed = set()
    crash_pos = None

    for i, (pos, direction, cross) in enumerate(carts):
        if i in crashed:
            continue
        del occupied[pos]

        next_pos = pos + direction
        next_track = track[next_pos]
        if next_track in ("\\", "/"):
            next_direction = TURNS[(track[next_pos], direction)]
            next_cross = cross
        elif next_track == "+":
            next_direction = CROSSINGS[(cross, direction)]
            next_cross = ROTATIONS[cross]
        else:
            next_direction = direction
            next_cross = cross

        if next_pos in occupied:
            crash_pos = next_pos
            j = occupied.pop(crash_pos)
            crashed |= {i, j}
            if not remove_crashed:
                return carts, crash_pos
        else:
            occupied[next_pos] = i
            next_carts[i] = (next_pos, next_direction, next_cross)

    if remove_crashed:
        next_carts = [cart for i, cart in enumerate(next_carts) if i not in crashed]

    return next_carts, crash_pos


@timer
def part1(data):
    track, carts = parse(data)

    while True:
        carts, crash_pos = tick(track, carts)
        if crash_pos is not None:
            return f"{int(crash_pos.real)},{int(crash_pos.imag)}"


@timer
def part2(data):
    track, carts = parse(data)

    while len(carts) > 1:
        carts, _ = tick(track, carts)

    remaining, *_ = carts[0]
    return f"{int(remaining.real)},{int(remaining.imag)}"


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)

    # ==== PART 1 ====
    print(part1(data))

    # ==== PART 2 ====
    print(part2(data))


if __name__ == "__main__":
    main()
