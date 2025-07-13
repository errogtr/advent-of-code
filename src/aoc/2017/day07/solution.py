from itertools import chain
from pathlib import Path
import re


SEP = " -> "
RE_WEIGHT = re.compile(r"(\w+)\s\((\d+)\)")
RE_LINKS = re.compile(r"\w+")


def traverse(current, links, weights):
    curr_weight = weights[current]
    
    if current not in links:
        return weights[current]

    subtree = [traverse(node, links, weights) for node in links[current]]
    assert len(set(subtree)) == 1, list(zip([weights[l] for l in links[current]], subtree))

    return curr_weight + sum(subtree)


def main(input_path: Path):
    with input_path.open() as f:
        raw_data = f.read()

    weights = dict()
    links = dict()
    for node_data in raw_data.splitlines():
        if SEP in node_data:
            src_data, links_data = node_data.split(SEP)
            node, weight = RE_WEIGHT.match(src_data).groups()
            links[node] = RE_LINKS.findall(links_data)
        else:
            node, weight = RE_WEIGHT.match(node_data).groups()
        weights[node] = int(weight)

    root = set(weights).difference(set(chain.from_iterable(links.values()))).pop()

    # ==== PART 1 ====
    print(root)

    # ==== PART 2 ====
    try:
        traverse(root, links, weights)
    except AssertionError as e:
        print(e)