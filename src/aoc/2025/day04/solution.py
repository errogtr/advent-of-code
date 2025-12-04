def accessible(z: complex, paper: set, nn: dict) -> bool:
    return sum(w in paper for w in nn[z]) < 4


def main():
    with open("src/aoc/2025/day04/data") as f:
        data = f.read()

    paper, nn = set(), dict()
    for y, row in enumerate(data.splitlines()):
        for x, c in enumerate(row):
            if c == "@":
                paper.add(x + 1j * y)
            nn[x + 1j * y] = [
                x + dx + 1j * (y + dy)
                for dx in (-1, 0, 1)
                for dy in (-1, 0, 1)
                if dx != 0 or dy != 0
            ]
    
    # ==== PART 1 ====
    print(sum(accessible(z, paper, nn) for z in paper))

    # ==== PART 2 ====
    count = len(paper)
    while True:
        removed = {z for z in paper if accessible(z, paper, nn)}
        if len(removed) == 0:
            break
        paper -= removed
    print(count - len(paper))
        

if __name__ == "__main__":
    main()
