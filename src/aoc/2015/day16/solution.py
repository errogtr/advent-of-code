def parse_compounds(s):
    quantities = [x.split(": ") for x in s.split(", ")]
    return dict((c, int(x)) for c, x in quantities)


with open("data") as f:
    aunts = [parse_compounds(l.split(": ", 1)[-1]) for l in f.read().splitlines()]

message = parse_compounds(
    "children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1"
)

# ==== PART 1 ====
print(
    next(
        n
        for n, aunt in enumerate(aunts, 1)
        if all(message[c] == x for c, x in aunt.items())
    )
)

# ==== PART 2 ====
print(
    next(
        n
        for n, aunt in enumerate(aunts, 1)
        if all(
            x > message[c]
            if c in {"cats", "trees"}
            else x < message[c]
            if c in {"pomeranians", "goldfish"}
            else x == message[c]
            for c, x in aunt.items()
        )
    )
)
