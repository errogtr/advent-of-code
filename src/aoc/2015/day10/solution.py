from itertools import groupby


def look_and_say(sequence, i):
    for _ in range(i):
        sequence = "".join(str(len(list(g))) + d for d, g in groupby(sequence))
    return sequence


with open("data") as f:
    sequence = f.read()

# ==== PART 1 ====
sequence = look_and_say(sequence, 40)
print(len(sequence))

# ==== PART 2 ====
print(len(look_and_say(sequence, 10)))
