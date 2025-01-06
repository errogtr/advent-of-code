from collections import Counter
from itertools import pairwise
from pathlib import Path


def parse(input_text: str) -> tuple[str, dict[str, str]]:
    template, rules = input_text.split("\n\n")
    insertions = dict(rule.split(" -> ") for rule in rules.split("\n"))
    return template, insertions


def insert(template: Counter, insertions: dict[str, str], n: int) -> Counter:
    pair_counts = Counter("".join(pair) for pair in pairwise(template))
    element_counts = Counter(template)
    for _ in range(n):
        insertion_counts = Counter()
        for (l, r), count in pair_counts.items():
            insertion = insertions[l + r]
            insertion_counts[l + insertion] += count
            insertion_counts[insertion + r] += count
            element_counts[insertion] += count
        pair_counts = insertion_counts
    most_common, *_, least_common = [c for _, c in element_counts.most_common()]
    return most_common - least_common


def main(input_path: Path):
    with input_path.open() as f:
        input_text = f.read()

    template, insertions = parse(input_text)

    # ==== PART 1 ====
    print(insert(template, insertions, 10))

    # ==== PART 2 ====
    print(insert(template, insertions, 40))
