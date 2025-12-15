def checksum(state):
    while len(state) % 2 == 0:
        state = "".join("1" if x == y else "0" for x, y in zip(state[::2], state[1::2]))
    return state


def fill(state, disk):
    while len(state) < disk:
        state += "0" + "".join("1" if x == "0" else "0" for x in state[::-1])
    return state[:disk]


with open("data") as f:
    state = f.read()

# ==== PART 1 ====
print(checksum(fill(state, 272)))

# ==== PART 2 ====
print(checksum(fill(state, 35651584)))
