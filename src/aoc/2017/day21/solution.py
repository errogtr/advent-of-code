from copy import deepcopy
import click

from aoc.utils import read_data


def print_img(img):
    print("\n".join("".join(line) for line in img), "\n")


def glue(img):
    return "/".join("".join(p) for p in img)


def separate(glued_img):
    return [list(line) for line in glued_img.split("/")]


def rotate(glued_img, rotations):
    img = separate(glued_img)
    size = len(img)
    for _ in range(rotations):
        rotated = [list() for _ in range(size)]
        for i in range(size):
            for j in range(size):
                rotated[i].append(img[size - j - 1][i])
        img = deepcopy(rotated)
    return glue(img)


def rotate_90(glued_img):
    return rotate(glued_img, rotations=1)


def rotate_180(glued_img):
    return rotate(glued_img, rotations=1)


def rotate_270(glued_img):
    return rotate(glued_img, rotations=1)


def flip_v(glued_img):
    img = separate(glued_img)
    size = len(img)
    flipped = [list() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            flipped[i].append(img[i][size - j - 1])
    return glue(flipped)


def flip_h(glued_img):
    img = separate(glued_img)
    size = len(img)
    flipped = [list() for _ in range(size)]
    for i in range(size):
        for j in range(size):
            flipped[i].append(img[size - i - 1][j])
    return glue(flipped)


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    rules = dict()
    for line in data.splitlines():
        src, dst = line.split(" => ")
        rules[src] = dst
        rules[rotate(src, 1)] = dst
        rules[rotate(src, 2)] = dst
        rules[rotate(src, 3)] = dst
        rules[flip_v(src)] = dst
        rules[rotate(flip_v(src), 1)] = dst
        rules[rotate(flip_v(src), 2)] = dst
        rules[rotate(flip_v(src), 3)] = dst
        rules[flip_h(src)] = dst
        rules[rotate(flip_h(src), 1)] = dst
        rules[rotate(flip_h(src), 2)] = dst
        rules[rotate(flip_h(src), 3)] = dst

    image = [list(".#."), list("..#"), list("###")]
    glued_img = glue(image)
    for src in [
        glued_img,
        rotate(glued_img),
        rotate(glued_img, 2),
        rotate(glued_img, 3),
        flip_v(glued_img),
        flip_h(glued_img),
    ]:
        if src in rules:
            dst = rules[src]
            rules[rotate(src, 1)] = dst
            rules[rotate(src, 2)] = dst
            rules[rotate(src, 3)] = dst
            rules[flip_v(src)] = dst
            rules[flip_h(src)] = dst
            break

    iterations = 18
    print_img(image)
    for _ in range(iterations):
        size = len(image)

        if size % 2 == 0:
            enhanced = [list() for _ in range((size // 2) * 3)]
            for i in range(0, size, 2):
                for j in range(0, size, 2):
                    patch = [
                        image[i][j : j + 2],
                        image[i + 1][j : j + 2],
                    ]
                    enhanced_patch = separate(rules[glue(patch)])
                    for k in range(3):
                        for l in range(3):
                            enhanced[k + 3 * (i // 2)].append(enhanced_patch[k][l])
        elif size % 3 == 0:
            enhanced = [list() for _ in range((size // 3) * 4)]
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    patch = [
                        image[i][j : j + 3],
                        image[i + 1][j : j + 3],
                        image[i + 2][j : j + 3],
                    ]
                    enhanced_patch = separate(rules[glue(patch)])
                    for k in range(4):
                        for l in range(4):
                            enhanced[k + 4 * (i // 3)].append(enhanced_patch[k][l])
        image = enhanced

    print(glue(image).count("#"))


if __name__ == "__main__":
    main()
