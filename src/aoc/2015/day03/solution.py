MOVES = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}


def next_house(move, p):
    return tuple(map(sum, zip(p, MOVES[move])))


def move_santa(n, moves):
    start = (0, 0)
    visited = {start}
    current = [start] * n
    for i, move in enumerate(moves):
        c = current[i % n] = next_house(move, current[i % n])
        visited.add(c)
    return len(visited)


with open("data") as f:
    moves = f.read()


# == PART 1 ==
print(move_santa(1, moves))

# == PART 2 ==
print(move_santa(2, moves))
