from pathlib import Path
from statistics import median

LEFT = "([{<"
RIGHT = ")]}>"
CLOSURES = dict(zip(LEFT, RIGHT))
OPENINGS = dict(zip(RIGHT, LEFT))
ERROR_SCORES = dict(zip(RIGHT, [3, 57, 1197, 25137]))
AUTOCOMPLETE_SCORES = dict(zip(LEFT, range(1, 5)))


def main(input_data: Path):
    with input_data.open() as f:
        lines = f.read().splitlines()

    error_score = 0
    autocomplete_scores = list()
    for line in lines:
        stack = list()
        for c in line:
            if c in CLOSURES:
                stack.append(c)
            elif CLOSURES[stack[-1]] == c:
                _ = stack.pop()
            else:
                error_score += ERROR_SCORES[c]
                break
        else:
            score = 0
            while stack:
                score = score * 5 + AUTOCOMPLETE_SCORES[stack.pop()]
            autocomplete_scores.append(score)

    # ==== PART 1 ====
    print(error_score)

    # ==== PART 2 ====
    print(median(autocomplete_scores))
