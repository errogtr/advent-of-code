from pathlib import Path
import re


Dot = tuple[int, int]
Fold = tuple[str, int]


def parse(input_text: str) -> tuple[set[Dot], list[Fold]]:
    dots_list, folds = input_text.split("\n\n")
    dots = {parse_coords(pair) for pair in dots_list.split("\n")}
    instructions = [(d, int(v)) for d, v in re.findall(r"(x|y)=(\d+)", folds)]
    return dots, instructions


def parse_coords(coords: str) -> Dot:
    x, y = coords.split(",")
    return int(x), int(y)


def fold(dots: set, instructions: list[Fold]) -> set:
    for how, val in instructions:
        folded = set()
        for x, y in dots:
            if how == "x":
                if x > val:
                    x = 2 * val - x
            else:  # how == "y"
                if y > val:
                    y = 2 * val - y
            folded.add((x, y))
        dots = folded
    return dots


def print_sheet(dots: set):
    Lx = max(x for x, _ in dots) + 1
    Ly = max(y for _, y in dots) + 1
    sheet = "\n".join(
        "".join("#" if (x, y) in dots else "." for x in range(Lx)) for y in range(Ly)
    )
    print(sheet)
    print()


def main(input_path: Path):
    with input_path.open() as f:
        input_text = f.read()

    dots, instructions = parse(input_text)

    # ==== PART 1 ====
    dots = fold(dots, [instructions[0]])
    print(len(dots))

    # ==== PART 2 ====
    dots = fold(dots, instructions[1:])
    print_sheet(dots)
