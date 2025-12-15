from functools import cache
from heapq import heappop, heappush
from itertools import combinations, product
import click
from aoc.utils import timer


@cache
def forbidden(state: tuple[int, ...]) -> bool:
    """Check if a state is invalid (microchip on same floor as non-paired generator)."""
    return any(
        state[chip_idx] == state[gen_idx]
        and state[gen_idx] != state[gen_idx + 1]
        and state[chip_idx] != state[chip_idx - 1]
        for chip_idx in range(1, len(state), 2)
        for gen_idx in range(0, len(state), 2)
        if chip_idx - 1 != gen_idx
    )


def normalize(state: tuple[int, ...]) -> tuple[int, ...]:
    """Convert state to normalized form by sorting pairs and then flatten again to recreate
    the original form. This handles symmetry: swapping identical pairs creates equivalent states,
    e.g. (2, 2, 1, 1, 3, 3), (3, 3, 2, 2, 1, 1) are the same state (1, 1, 2, 2, 3, 3)"""
    pairs = tuple((state[i], state[i + 1]) for i in range(0, len(state), 2))
    return tuple(floor for pair in sorted(pairs) for floor in pair)


def elevator(start: tuple[int, ...]) -> int:
    """Find minimum steps to move all items to floor 4 using Dijkstra."""
    current_steps = 0
    current_floor = 1
    current_state = normalize(start)

    queue = [(current_steps, current_floor, current_state)]
    visited = {(current_floor, current_state)}

    num_objects = len(start)
    target_state = tuple([4] * num_objects)

    while queue:
        current_steps, current_floor, current_state = heappop(queue)

        if current_state == target_state:
            break

        # Find all items on the current floor
        items_on_floor = [
            item_idx
            for item_idx, item_floor in enumerate(current_state)
            if item_floor == current_floor
        ]

        # Try moving 1 or 2 items, going up or down
        for num_items_to_move, floor_direction in product((1, 2), (-1, 1)):
            for selected_items in combinations(items_on_floor, num_items_to_move):
                next_floor = current_floor + floor_direction

                # Check floor bounds
                if not (1 <= next_floor <= 4):
                    continue

                # Create new state with selected items moved
                new_state = tuple(
                    item_floor + floor_direction
                    if item_idx in selected_items
                    else item_floor
                    for item_idx, item_floor in enumerate(current_state)
                )

                # Skip if state violates safety rules
                if forbidden(new_state):
                    continue

                # Normalize and check if we've visited this state before
                normalized_new_state = normalize(new_state)
                if (next_floor, normalized_new_state) not in visited:
                    heappush(
                        queue, (current_steps + 1, next_floor, normalized_new_state)
                    )
                    visited.add((next_floor, normalized_new_state))

    return current_steps


@timer
def part1(start: tuple[int, ...]) -> int:
    return elevator(start)


@timer
def part2(start: tuple[int, ...]) -> int:
    return elevator(start + (1, 1, 1, 1))


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    state = (1, 2, 3, 1) if example else (1, 1, 1, 2, 1, 2, 3, 3, 3, 3)

    # ==== PART 1 ====
    print(part1(state))

    # ==== PART 2 ====
    print(part2(state))


if __name__ == "__main__":
    main()
