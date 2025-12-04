NEIGH = [dx + 1j * dy for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0]


def nn(z: complex):
    for dz in NEIGH:
        yield z + dz


def accessible(z: complex, paper: set) -> bool:
    return sum(w in paper for w in nn(z)) < 4


def main():
    with open("src/aoc/2025/day04/data") as f:
        data = f.read()

    paper = set()
    for y, row in enumerate(data.splitlines()):
        for x, c in enumerate(row):
            if c == "@":
                paper.add(x + 1j * y)

    # ==== PART 1 ====
    print(sum(accessible(z, paper) for z in paper))

    # ==== PART 2 ====
    count = len(paper)
    while True:
        removed = {z for z in paper if accessible(z, paper)}
        if len(removed) == 0:
            break
        paper -= removed
    print(count - len(paper))


if __name__ == "__main__":
    main()
