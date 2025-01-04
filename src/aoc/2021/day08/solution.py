from pathlib import Path
from collections import Counter

# Each number in 7-digits display can be uniquely mapped to an integer as follows.
# - Count occurrences for each segment (a to g) in all digits (0-9):
#   * Segment `a` lights up in the digits 0, 2, 3, 5, 6, 7, 8, 9. It appears 8 times.
#   * Segment `b` lights up in the digits 0, 4, 5, 6, 8, 9. It appears 6 times.
#   * Segment `c` lights up in the digits 0, 1, 2, 3, 4, 7, 8, 9. It appears 8 times.
#   * Segment `d` lights up in the digits 2, 3, 4, 5, 6, 8, 9. It appears 7 times.
#   * Segment `e` lights up in the digits 0, 2, 6, 8. It appears 4 times.
#   * Segment `f` lights up in the digits 0, 1, 3, 4, 5, 6, 7, 8, 9. It appears 9 times.
#   * Segment `g` lights up in the digits 0, 2, 3, 5, 6, 8, 9. It appears 7 times.
# - For each digit, calculate the sum of the segment occurrence counts for the segments that make up the digit, e.g.:
#   * The digit `0` is formed by segments `a, b, c, e, f, g`. The sum of segment counts for `0` is:
#       8 (a) + 6 (b) + 8 (c) + 4 (e) + 9 (f) + 7 (g) = 42
#   * The digit `7` is formed by segments `a, c, f`. The sum of segment counts for `7` is:
#       8 (a) + 8 (c) + 9 (f) = 25
#   * Similarly, for other digits, we sum the occurrences of the corresponding segments.
# - Using these sums, we can map each unique sum to its corresponding digit. This is done in the DECODER dictionary, e.g.:
#   * Sum of 42 corresponds to digit `0`
#   * Sum of 25 corresponds to digit `7`
#   * And so on...
DECODER = dict(zip([42, 17, 34, 39, 30, 37, 41, 25, 49, 45], "0123456789"))


def parse(line: str) -> tuple[list[str], list[frozenset]]:
    signals, outputs = line.split(" | ")
    frozen_outs = [frozenset(out) for out in outputs.split()]
    return signals.split(), frozen_outs


def main(input_data: Path):
    with input_data.open() as f:
        data = f.read().splitlines()

    easy_digits = 0
    total = 0
    for line in data:
        signals, outputs = parse(line)
        wires_count = Counter("".join(signals))
        encoded = {frozenset(s): sum(wires_count[d] for d in s) for s in signals}
        decoded = "".join(DECODER[encoded[out]] for out in outputs)
        easy_digits += sum(d in ("1478") for d in decoded)
        total += int(decoded)

    # ==== PART 1 ====
    print(easy_digits)

    # ==== PART 2 ====
    print(total)
