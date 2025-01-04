from pathlib import Path


def main(input_data: Path):
    with input_data.open() as f:
        data = f.read().splitlines()

    c = 0
    for line in data:
        signals, outputs = line.split(" | ")
        c += sum(len(o) in {2, 3, 4, 7} for o in outputs.split())

    
    print(c)