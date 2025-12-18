from itertools import combinations
import re
import click
from aoc.utils import read_data, timer


Coords = tuple[int, int]
Node = tuple[int, int]


NODE_PATTERN = re.compile(r"x(\d+)-y(\d+)+\s+\d+T\s+(\d+)T\s+(\d+)T")


def parse_node(line: str) -> tuple[Coords, Node]:
    node_data = NODE_PATTERN.search(line)

    if node_data is None:
        raise RuntimeError("Failed to parse node.")

    x, y, used, available = map(int, node_data.groups())
    return (x, y), (used, available)


@timer
def part1(nodes: dict[Coords, Node]) -> int:
    viable = 0
    for (used_A, available_A), (used_B, available_B) in combinations(nodes.values(), 2):
        viable += (0 < used_A <= available_B) + (0 < used_B <= available_A)
    return viable


@timer
def part2(nodes: dict[Coords, Node]) -> int:
    """
    Solved with pen and paper. The input is something like the following:

    (.) .  .  .  .  .  .  G    <--- goal data are at x_goal, 0
     .  .  .  .  .  .  .  .
     .  .  #  #  #  #  #  #    <--- "wall" of very large, very full nodes, starting at x_wall
     .  .  .  .  .  .  .  .
     .  .  .  .  .  .  .  .    <--- the other nodes have enough capacity to swap memory with the empty node
     .  .  .  .  .  .  .  .
     .  .  .  .  .  _  .  .    <--- single empty node (position x_empty, y_empty)
     .  .  .  .  .  .  .  .

           ^
           |
           x_wall

    The route with fewer steps is the "straightest" possible which goes around the wall of full nodes
    and reaches the goal data, swapping memory with it, that is:

    (.) O  O  O  O  O  G  _     <--- The "route" of empty node is marked as "O". It reaches
     .  O  .  .  .  .  .  .          the goal data and moves them in the neighboring node
     .  O  #  #  #  #  #  #
     .  O  .  .  .  .  .  .
     .  O  .  .  .  .  .  .
     .  O  .  .  .  .  .  .
     .  O  O  O  O  O  .  .
     .  .  .  .  .  .  .  .

    From now on, the fewest steps to move the goal data to the node x0, y0 is by shuffling with
    mini-cycles of 5 steps each, (x_goal - 1) times. Something like:

     .  G  _   =>  .  G  .  =>  .  G  .  =>  .  G  .  =>  _  G  .  =>  G  _  .
     .  .  .       .  .  _      .  _  .      _  .  .      .  .  .      .  .  .

                      1            2            3            4            5


    The fewest number of steps required to move the goal data is then:

        x_empty - (x_wall - 1)      <--- steps from empty node and "left of the wall" at y_empty
      + y_empty                     <--- steps from "left of the wall" at y_empty to y=0
      + x_goal - (x_wall - 1)       <--- steps from x_empty to x_goal
      + 5 * (x_goal - 1)            <--- shuffling steps

      = 2 * (x_empty - (x_wall - 1)) + y_empty + (x_goal - x_empty) + 5 * (x_goal - 1)

    For my input:

        x_wall = 6

    """

    x_empty, y_empty = next((x, y) for (x, y), (used, _) in nodes.items() if used == 0)
    x_goal = max(x for x, _ in nodes)
    x_wall = 6

    steps_empty_to_wall = x_empty - (x_wall - 1)
    steps_wall_to_goal = x_goal - (x_wall - 1)

    return steps_empty_to_wall + steps_wall_to_goal + y_empty + 5 * (x_goal - 1)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)
    nodes = dict(parse_node(line) for line in data.splitlines()[2:])

    # ==== PART 1 ====
    print(part1(nodes))

    # ==== PART 2 ====
    print(part2(nodes))


if __name__ == "__main__":
    main()
