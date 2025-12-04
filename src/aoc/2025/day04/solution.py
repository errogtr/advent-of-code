from aoc.utils import timer


NEIGH = [dx + 1j * dy for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0]


def nn(z: complex):
    for dz in NEIGH:
        yield z + dz


def accessible(z: complex, paper: set) -> bool:
    return sum(w in paper for w in nn(z)) < 4


@timer
def part1(paper):
    return sum(accessible(z, paper) for z in paper)


@timer
def part2(paper):
    papers_count = len(paper)
    q = list(paper)
    while q:
        z = q.pop()
        if z not in paper:
            continue
        if accessible(z, paper):
            paper.remove(z)
            for w in nn(z):
                q.append(w)
    return papers_count - len(paper)


def main():
    with open("src/aoc/2025/day04/data") as f:
        data = f.read()

    paper = set()
    for y, row in enumerate(data.splitlines()):
        for x, c in enumerate(row):
            if c == "@":
                paper.add(x + 1j * y)

    # ==== PART 1 ====
    print(part1(paper))

    # ==== PART 2 ====
    print(part2(paper))


if __name__ == "__main__":
    main()
