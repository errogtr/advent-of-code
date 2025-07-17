from pathlib import Path


def main(input_path: Path):
    with input_path.open() as f:
        stream = f.read()

    scores_depth = list()
    score = 0
    total_garbage = 0
    garbage = False
    while stream:
        c, stream = stream[0], stream[1:]

        if c == "!":
            stream = stream[1:]
        elif garbage:
            if c == ">":
                garbage = False
            else:
                total_garbage += 1
        elif c == "<":
            garbage = True
        elif c == "{":
            scores_depth.append(scores_depth[-1] + 1 if scores_depth else 1)
        elif c == "}":
            score += scores_depth.pop()

    # ==== PART 1 ====
    print(score)

    # ==== PART 2 ====
    print(total_garbage)
