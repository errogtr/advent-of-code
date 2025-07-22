from pathlib import Path


def main(input_path: Path):
    with input_path.open() as f:
        steps = int(f.read())

    buffer, curr, target = [0], 0, 0
    for t in range(1, 50_000_000):
        curr = (curr + steps) % t + 1
        if t <= 2017:
            buffer.insert(curr, t)
        if curr == 1:
            target = t

    # ==== PART 1 ====
    print(buffer[buffer.index(2017) + 1])

    # ==== PART 2 ====
    print(target)
