from typing import Counter
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
    carts = sorted(carts, key=lambda cart: cart[0].imag)
    return track, carts


def tick(track, carts):
    next_carts = []
    for pos, direction, cross in carts:
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
        next_carts.append((next_pos, next_direction, next_cross))
    return sorted(next_carts, key=lambda cart: cart[0].imag)


@timer
def part1(data):
    track, carts = parse(data)

    while True:
        carts = tick(track, carts)
        pos_counter = Counter(cart[0] for cart in carts)
        if any(c > 1 for c in pos_counter.values()):
            crash = pos_counter.most_common(1)[0][0]
            return f"{int(crash.real)},{int(crash.imag)}"


@timer
def part2(data):
    track, carts = parse(data)

    while len(carts) > 1:
        carts = tick(track, carts)

        counts = Counter(cart[0] for cart in carts)
        crashes = list()
        for i, cart in enumerate(carts):
            pos, *_ = cart
            if counts[pos] > 1:
                crashes.append(i)

        carts = [cart for i, cart in enumerate(carts) if i not in crashes]

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
