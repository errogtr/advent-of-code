def execute(registers):
    current = 0
    while current < len(instructions):
        instruction, *args = instructions[current].split()
        match instruction:
            case "cpy":
                val = registers[args[0]] if args[0] in registers else int(args[0])
                registers[args[1]] = val
            case "jnz":
                cmp = registers[args[0]] if args[0] in registers else int(args[0])
                current += int(args[1]) - 1 if cmp != 0 else 0
            case "inc":
                registers[args[0]] += 1
            case "dec":
                registers[args[0]] -= 1
        current += 1
    return registers["a"]


with open("data") as f:
    instructions = f.read().splitlines()

# ==== PART 1 ====
print(execute({"a": 0, "b": 0, "c": 0, "d": 0}))

# ==== PART 2 ====
print(execute({"a": 0, "b": 0, "c": 1, "d": 0}))
