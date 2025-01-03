with open("data") as f:
    prisms = [[int(x) for x in l.split("x")] for l in f.read().splitlines()]


# == PART 1 ==
print(sum(2 * (l * w + l * h + w * h) + min(l * w, l * h, w * h) for l, w, h in prisms))

# == PART 2 ==
print(sum(l * w * h + 2 * min(l + w, l + h, w + h) for l, w, h in prisms))
