import click
from aoc.utils import read_data, timer


@timer
def part1(data):
    elves = [0, 1]
    recipes = [3, 7]
    board = [3, 7]
    while len(board) < int(data) + 10:
        tens, units = divmod(sum(recipes), 10)
        digits = (tens, units) if tens else (units,)
        for digit in digits:
            board.append(digit)

        for i in (0, 1):
            elves[i] = (elves[i] + recipes[i] + 1) % len(board)
            recipes[i] = board[elves[i]]

    return "".join(str(score) for score in board[int(data):int(data) + 10])


@timer
def part2(data):
    sequence = [int(x) for x in data]
    elves = [0, 1]
    recipes = [3, 7]
    board = [3, 7]
    while True:
        tens, units = divmod(sum(recipes), 10)
        digits = (tens, units) if tens else (units,)
        for digit in digits:
            board.append(digit)
            if board[-len(sequence):] == sequence:
                return len(board) - len(sequence)

        for i in (0, 1):
            elves[i] = (elves[i] + recipes[i] + 1) % len(board)
            recipes[i] = board[elves[i]]


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
