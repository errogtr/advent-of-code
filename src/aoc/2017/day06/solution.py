from pathlib import Path


def state(blocks: list[int]) -> str:
    """ A state is a string representation of a list of memory blocks """
    return "".join(str(b) for b in blocks)


def main(input_path: Path):
    with input_path.open() as f:
        blocks = [int(x) for x in f.read().split()]
    
    # this is the crucial data structure: seen = {'state': 'first appearance'}
    seen = dict()
    cycles = 0
    while (s := state(blocks)) not in seen:
        seen[s] = cycles
        max_val = max(blocks)
        i = blocks.index(max_val)
        blocks[i] = 0
        while max_val:  # I think this can be optimized
            i = (i + 1) % len(blocks)
            blocks[i] += 1
            max_val -= 1
        cycles += 1
    
    # ==== PART 1 ====
    print(cycles)

    # ==== PART 2 ====
    print(cycles - seen[s])

