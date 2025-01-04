from pathlib import Path

DIRS = [1, 1j, -1, -1j]


def parse(input_text: str) -> dict:
    heightmap = dict()
    for y, row in enumerate(input_text.splitlines()):
        for x, val in enumerate(row):
            heightmap[x + y * 1j] = int(val)
    return heightmap


def get_nns(z):
    return [z + dz for dz in DIRS]


def main(input_data: Path):
    with input_data.open() as f:
        input_text = f.read()
    heightmap = parse(input_text)

    all_nns = {z: get_nns(z) for z in heightmap}

    # ==== PART 1 ====
    low_points = list()
    for z, height in heightmap.items():
        if all(heightmap.get(w, 9) > height for w in all_nns[z]):
            low_points.append(z)

    print(sum(1 + heightmap[z] for z in low_points))
