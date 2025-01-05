from pathlib import Path


CLOSURES = dict(zip("([{<", ")]}>"))
ERROR_SCORES = dict(zip(")]}>", [3, 57, 1197, 25137]))


def main(input_data: Path):
    with input_data.open() as f:
        lines = f.read().splitlines()

    error_score = 0
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
    
    print(error_score)
