from pathlib import Path


def print_img(img):
    print("\n".join("".join(line) for line in img), "\n")


def main(input_path: Path):
    with input_path.open() as f:
        data_raw = f.read().splitlines()

    rules = dict()
    for line in data_raw:
        src, dst = line.split(" => ")
        rules[src] = dst
    
    image = [list(".#."), list("..#"), list(".##")]
    iterations = 1
    for _ in range(iterations):
        size = len(image)
        if size % 2 == 0:
            ...
        elif size % 3 == 0:
            patches = list()
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    patch = [image[i][j:j+3], image[i+1][j:j+3], image[i+2][j:j+3]]
                    patches.append(patch)
                    print_img(patch)
