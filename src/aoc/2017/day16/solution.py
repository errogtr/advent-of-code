from pathlib import Path


def swap(programs, x, y):
    seq = list(programs)
    seq[x], seq[y] = seq[y], seq[x]
    return "".join(seq)


def main(input_path: Path):
    with input_path.open() as f:
        moves = f.read()

    programs = "abcdefghijklmnop"
    visited = [programs]
    while True:
        for move in moves.split(","):
            if move.startswith("s"):
                spin = int(move[1:])
                programs = programs[-spin:] + programs[:-spin]
            else:
                specs = move[1:].split("/")
                if move.startswith("x"):
                    x, y = map(int, specs)
                elif move.startswith("p"):
                    x, y = map(programs.index, specs)
                programs = swap(programs, x, y)

        if "".join(programs) in visited:
            break

        visited.append("".join(programs))

    # ==== PART 1 ====
    print(visited[1])

    # ==== PART 2 ====
    print(visited[1_000_000_000 % len(visited)])
