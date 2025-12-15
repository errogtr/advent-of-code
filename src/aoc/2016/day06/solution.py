from collections import Counter


def count_bits(bits, idx):
    return Counter(bits).most_common().pop(idx)[0]


with open("data") as f:
    messages = f.read().splitlines()


# ==== PART 1 ====
print("".join(count_bits(bits, 0) for bits in zip(*messages)))

# ==== PART 2 ====
print("".join(count_bits(bits, -1) for bits in zip(*messages)))
