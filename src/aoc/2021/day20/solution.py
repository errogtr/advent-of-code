from copy import deepcopy
from itertools import product
from pathlib import Path


Img = list[list[str]]


def parse(input_raw: str) -> tuple[str, Img]:
    enhancement_raw, img_raw = input_raw.split("\n\n")

    enhancement = ["0" if c == "." else "1" for c in enhancement_raw]

    img = [
        ["0" if pixel == "." else "1" for pixel in row] for row in img_raw.splitlines()
    ]
    return enhancement, img


def pad(img: Img, padding: int) -> Img:
    padded_lr = [["0"] * padding + row + ["0"] * padding for row in img]

    lx = len(padded_lr[0])
    padded_ud = [["0"] * lx] * padding + padded_lr + [["0"] * lx] * padding
    return padded_ud


def idx(x: int, y: int, img: Img) -> Img:
    binarized = "".join(img[y + dy][x + dx] for dy, dx in product((-1, 0, 1), repeat=2))
    return int(binarized, 2)


def enhance(img: Img, enhancement: str) -> Img:
    lx = len(img[0]) - 1
    ly = len(img) - 1

    return [[enhancement[idx(x, y, img)] for x in range(1, lx)] for y in range(1, ly)]


def main(input_path: Path):
    with input_path.open() as f:
        enhanchement, input_img = parse(f.read())

    img = deepcopy(input_img)
    for _ in range(2):
        img = enhance(pad(img, 2), enhanchement)
    print(sum(p == "1" for row in img for p in row))
