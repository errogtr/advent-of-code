from hashlib import md5
from heapq import heappop, heappush

import click
from aoc.utils import read_data, timer


DIRECTIONS = [(-1j, "U"), (1j, "D"), (-1, "L"), (1, "R")]


def in_grid(z: complex) -> bool:
    return 0 <= z.real <= 3 and 0 <= z.imag <= 3


def is_unlocked(char: str) -> bool:
    return char in "bcdef"


def find_path(passcode: str, longest: bool) -> tuple[str, int]:
    current_steps = 0
    current_passcode = passcode
    current_room = 0 + 0 * 1j

    queue = [(current_steps, (current_passcode, current_room))]
    visited = set()
    max_length = 0
    while queue:
        current_steps, (current_passcode, current_room) = heappop(queue)

        if current_room == 3 + 3j:
            max_length = max(current_steps, max_length)
            if longest:
                continue
            break

        md5_control_chars = md5(current_passcode.encode()).hexdigest()[:4]
        for dir_idx, char in enumerate(md5_control_chars):
            dir_grid, dir_char = DIRECTIONS[dir_idx]
            next_room = current_room + dir_grid
            next_passcode = current_passcode + dir_char
            next_state = (next_passcode, next_room)
            if in_grid(next_room) and is_unlocked(char) and next_state not in visited:
                heappush(queue, (current_steps + 1, next_state))
                visited.add(next_state)

    return current_passcode[len(passcode) :], max_length


@timer
def part1(passcode: str) -> str:
    path, _ = find_path(passcode, longest=False)
    return path


@timer
def part2(passcode: str) -> int:
    _, length = find_path(passcode, longest=True)
    return length


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
