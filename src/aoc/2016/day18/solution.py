import click
from aoc.utils import read_data, timer


def safe_tiles(row_str: str, n_rows: int) -> int:
    """Count safe tiles using Rule 90 cellular automaton.
    
    Rule 90 (https://tinyurl.com/4herwm62) generates each row by taking the XOR 
    between characters in even and odd positions. Using integers, this is 
    equivalent to XORing a left-shifted integer (with MSB masked off) with the 
    same integer right-shifted.
    """
    size = len(row_str)
    mask = (1 << size) - 1

    row = int(row_str.replace("^", "1").replace(".", "0"), 2)
    safe_tiles_count = size - bin(row).count("1")
    for _ in range(n_rows - 1):
        row = ((row << 1) ^ (row >> 1)) & mask
        safe_tiles_count += size - bin(row).count("1")
    return safe_tiles_count


@timer
def part1(row_str: str, n_rows: int) -> int:
    return safe_tiles(row_str, n_rows)


@timer
def part2(row_str: str, n_rows: int) -> int:
    return safe_tiles(row_str, 10_000 * n_rows)


@click.command()
@click.option("--example", is_flag=True)
def main(example: bool):
    data = read_data(__file__, example)
    n_rows = 10 if example else 40

    # ==== PART 1 ====
    print(part1(data, n_rows))

    # ==== PART 2 ====
    print(part2(data, n_rows))


if __name__ == "__main__":
    main()
