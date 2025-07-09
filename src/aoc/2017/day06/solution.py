from pathlib import Path


def main(input_path: Path):
    with input_path.open() as f:
        blocks = dict(enumerate(map(int, f.read().split())))
    

    seen = {"".join(map(str, blocks.values())): 0}
    cycles = 1
    while True:
        i, max_val = max(blocks.items(), key=lambda x: x[1])
        blocks[i] = 0
        while max_val:
            i = (i + 1) % len(blocks)
            blocks[i] += 1
            max_val -= 1
        state = "".join(map(str, blocks.values()))
        if state in seen:
            break
        seen[state] = cycles
        cycles += 1
    
    print(cycles)

    print(cycles - seen[state])

