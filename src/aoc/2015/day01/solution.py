def counts(instructions):
    return instructions.count("(") - instructions.count(")")


with open("data") as f:
    instructions = f.read()

# == PART 1 ==
print(counts(instructions))

# == PART 2 ==
print(next(i for i in range(len(instructions)) if counts(instructions[:i]) == -1))
