from collections import Counter
from itertools import pairwise
from pathlib import Path


def parse(input_text: str) -> tuple[str, dict[str, str]]:
    template, rules = input_text.split("\n\n")
    insertions = dict(rule.split(" -> ") for rule in rules.split("\n"))
    return template, insertions


def insert(pair_counts: Counter, insertions: dict[str, str], n: int) -> Counter:
    for _ in range(n):
        insertion_counts = Counter()
        for (l, r), count in pair_counts.items():
            pair_l = l + insertions[l + r]
            pair_r = insertions[l + r] + r
            insertion_counts[pair_l] += count
            insertion_counts[pair_r] += count
        pair_counts = insertion_counts
    return pair_counts


def elements(pair_counts: Counter, first: str, last: str) -> int:
    element_counts = Counter({first: 1, last: 1})
    for (l, r), count in pair_counts.items():
        element_counts[l] += count
        element_counts[r] += count   
    most_common, *_, least_common = [c // 2 for _, c in element_counts.most_common()]
    return most_common - least_common


def main(input_path: Path):
    with input_path.open() as f:
        input_text = f.read()

    template, insertions = parse(input_text)
    first, *_, last = template
    template_counts = Counter("".join(pair) for pair in pairwise(template))

    # ==== PART 1 ====
    print(elements(insert(template_counts, insertions, 10), first, last))

    # ==== PART 2 ====
    print(elements(insert(template_counts, insertions, 40), first, last))
