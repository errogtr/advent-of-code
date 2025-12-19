import click
from aoc.utils import read_data, timer


def extract_register(instruction: str) -> int:
    return int(instruction.split()[1])


@timer
def part1(b: int, c: int) -> int:
    """Find the minimum value of 'a' that generates an alternating 0,1,0,1... output.

    The assembly program repeatedly divides (a + b*c) by 2 and outputs the remainder.
    To produce an alternating sequence of 0,1,0,1..., we need (a + b*c) to have
    alternating bits in its binary representation: ...10101010, equivantly we need
        - a + b * c                     even
        - (a + b * c) // 2              odd
        - (a + b * c // 2) // 2         even
        - ...
        - 1
        - 0

    When a + b * c has been divided enough times to get to 0, the program restarts.

    This constructs such a number by starting at 1 and building upward: if the current
    value is odd, double it (append a 0 bit); if even, double and add 1 (append a 1 bit).
    This creates the alternating bit pattern. Once the value exceeds b*c, subtract b*c
    to find the minimum 'a'.
    """

    target = 1
    while target < b * c:
        target = 2 * target + (target % 2 == 0)
    return target - b * c


@timer
def part2():
    return "Merry Christmas! 🎄"


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)
    instructions = data.splitlines()
    b = extract_register(instructions[1])
    c = extract_register(instructions[2])

    # ==== PART 1 ====
    print(part1(b, c))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()


# ============================================================================
# Original simulation code (preserved for reference)
# ============================================================================
# This was the initial solution before discovering the factorial pattern.
#
# def part1(instructions: list[str], registers: dict[str, int]) -> int:
#     current = 0
#     while current < len(instructions):
#         instruction, *args = instructions[current].split()
#         match instruction:
#             case "cpy":
#                 val = registers[args[0]] if args[0] in registers else int(args[0])
#                 registers[args[1]] = val
#             case "jnz":
#                 cmp = registers[args[0]] if args[0] in registers else int(args[0])
#                 current += int(args[1]) if cmp != 0 else 1
#                 continue
#             case "inc":
#                 registers[args[0]] += 1
#             case "dec":
#                 registers[args[0]] -= 1
#             case "out":
#                 print(registers[args[0]])
#         current += 1
#     return registers["a"]
