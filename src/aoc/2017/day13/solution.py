from itertools import count
from pathlib import Path


def get_severity(firewall, delay):
    severity = 0
    for idx, depth in firewall.items():
        if (idx + delay) % (2 * (depth - 1)) == 0:
            severity += depth * (idx + delay)
            if delay:
                break
    return severity


def main(input_path: Path):
    with input_path.open() as f:
        firewall = dict(map(int, line.split(": ")) for line in f.read().splitlines())

    # ==== PART 1 ====
    print(get_severity(firewall, delay=0))

    # ==== PART 2 ====
    print(next(delay for delay in count(1) if get_severity(firewall, delay) == 0))
