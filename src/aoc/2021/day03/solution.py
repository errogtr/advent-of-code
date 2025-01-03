from operator import ge, lt


def get_most_common(col, op):
    return op(sum(col), len(col) / 2)


def counts(data, op):
    cols = [[int(x) for x in col] for col in zip(*data)]
    binary = "".join("1" if get_most_common(col, op) else "0" for col in cols)
    return int(binary, 2)


def rating(data, op, i=0):
    if len(data) == 1:
        return int(data[0], 2)

    col = [int(row[i]) for row in data]
    most_common = "1" if get_most_common(col, op) else "0"
    return rating([b for b in data if b[i] == most_common], op, i + 1)


with open("data") as f:
    data = f.read().splitlines()

# ==== PART 1 ====
print(counts(data, ge) * counts(data, lt))

# ==== PART 2 ====
print(rating(data, ge) * rating(data, lt))
