from pathlib import Path


def main(input_path: Path):
    with input_path.open() as f:
        steps = int(f.read())

    # ==== PART 1 ====
    buffer, curr = [0], 0
    for t in range(1, 2018):
        curr = (curr + steps) % t + 1
        buffer.insert(curr, t)
    print(buffer[buffer.index(2017) + 1])

    # ==== PART 2 ====
    target = 0
    for t in range(2018, 50_000_000):
        curr = (curr + steps) % t + 1
        if curr == 1:
            target = t
    print(target)
