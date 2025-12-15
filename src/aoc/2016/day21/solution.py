import re
from itertools import permutations


def scramble(password, instructions):
    for instruction in instructions:
        action, specs = instruction.split(" ", 1)
        match action:
            case "move":
                x, y = map(int, re.findall(r"(\d+)", specs))
                password.insert(y, password.pop(x))
            case "reverse":
                x, y = map(int, re.findall(r"(\d+)", specs))
                password = password[:x] + password[x : y + 1][::-1] + password[y + 1 :]
            case "rotate":
                if specs.startswith("based"):
                    idx = password.index(specs[-1])
                    steps = 1 + idx + (idx >= 4)
                else:
                    steps = int(re.search(r"\d+", specs).group())
                rotations = (-1) ** ("left" not in specs) * (steps % len(password))
                password = password[rotations:] + password[:rotations]
            case "swap":
                if specs.startswith("letter"):
                    x, y = re.search(r"letter (\w+) with letter (\w+)", specs).groups()
                    i, j = password.index(x), password.index(y)
                else:
                    i, j = map(int, re.findall(r"\d+", specs))
                password[i], password[j] = password[j], password[i]
    return "".join(password)


with open("data") as f:
    instructions = f.read().splitlines()

abcdefgh = list("abcdefgh")

# ==== PART 1 ====
print(scramble(abcdefgh, instructions))

# ==== PART 2 ====
scrambled = "fbgdceah"
for password in permutations(abcdefgh):
    if scramble(list(password), instructions) == scrambled:
        print("".join(password))
        break
