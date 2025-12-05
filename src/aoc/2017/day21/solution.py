import click

from aoc.utils import read_data, timer


def glue(img):
    return "/".join("".join(p) for p in img)


def separate(glued_img):
    return [list(line) for line in glued_img.split("/")]


def rotate(glued_img):
    img = separate(glued_img)
    rotated = list(zip(*img[::-1]))
    return glue(rotated)


def flip_v(glued_img):
    img = separate(glued_img)
    flipped = img[::-1]
    return glue(flipped)


def flip_h(glued_img):
    img = separate(glued_img)
    flipped = [row[::-1] for row in img]
    return glue(flipped)


def enhance(img, img_size, s, rules):
    enhanced = [list() for _ in range((img_size // s) * (s + 1))]
    for i in range(0, img_size, s):
        for j in range(0, img_size, s):
            patch = [row[j : j + s] for row in img[i : i + s]]
            enhanced_patch = separate(rules[glue(patch)])
            for k in range((s + 1)):
                for l in range((s + 1)):
                    enhanced[k + (s + 1) * (i // s)].append(enhanced_patch[k][l])
    return enhanced


def iterate(rules, iterations):
    image = [list(".#."), list("..#"), list("###")]

    for _ in range(iterations):
        size = len(image)
        if size % 2 == 0:
            image = enhance(image, size, 2, rules)
        elif size % 3 == 0:
            image = enhance(image, size, 3, rules)

    return glue(image).count("#")


@timer
def part1(rules):
    return iterate(rules, 5)


@timer
def part2(rules):
    return iterate(rules, 18)


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    rules = dict()
    for line in data.splitlines():
        src, dst = line.split(" => ")
        for _ in range(4):
            src = rotate(src)
            rules[src] = dst
            rules[flip_h(src)] = dst
            rules[flip_v(src)] = dst

    # ==== PART 1 ====
    print(part1(rules))

    # ==== PART 2 ====
    print(part2(rules))


if __name__ == "__main__":
    main()
