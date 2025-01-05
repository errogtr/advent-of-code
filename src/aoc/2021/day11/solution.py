from itertools import count
from pathlib import Path


DIRS = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]


def parse(grid: str) -> dict[complex, int]:
    octopus = dict()
    for y, row in enumerate(grid.splitlines()):
        for x, val in enumerate(row):
            octopus[x + y * 1j] = int(val)
    return octopus


def get_nns(z: complex, sites: set) -> list[complex]:
    return [z + dz for dz in DIRS if z + dz in sites]


def main(input_data: Path):
    with input_data.open() as f:
        input_grid = f.read()

    octopus = parse(input_grid)

    all_nns = {z: get_nns(z, set(octopus)) for z in octopus}
    
    flashes = 0
    for t in count(1):
        octopus = {z: energy + 1 for z, energy in octopus.items()}

        flashing = [z for z, energy in octopus.items() if energy > 9]
        flashed = set(flashing)
        while flashing:
            z_flash = flashing.pop(0)
            
            for w in all_nns[z_flash]:
                octopus[w] += 1
                if octopus[w] > 9 and w not in flashed:
                    flashed.add(w)
                    flashing.append(w)
        
        for z in flashed:
            octopus[z] = 0

        flashes += len(flashed)

        # ==== PART 1 ====
        if t == 100:
            print(flashes)

        # ==== PART 2 ====
        if len(flashed) == len(octopus):
            print(t)
            break
