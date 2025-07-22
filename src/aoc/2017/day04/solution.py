from pathlib import Path


def sort(l):
    return ["".join(sorted(w)) for w in l]


def main(input_path: Path):
    with input_path.open() as f:
        passphrases = [l.split() for l in f.readlines()]

    # ==== PART 1 ====
    print(sum(len(l) == len(set(l)) for l in passphrases))

    # ==== PART 2 ====
    print(sum(len(sort(l)) == len(set(sort(l))) for l in passphrases))

