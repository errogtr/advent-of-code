def exec(registers, instructions):
    current = 0
    while current < len(instructions):
        name, *args = instructions[current].split()
        match name:
            case "hlf":
                registers[args[0]] /= 2
            case "tpl":
                registers[args[0]] *= 3
            case "inc":
                registers[args[0]] += 1
            case "jmp":
                current += int(args[0]) - 1
            case "jie":
                if registers[args[0]] % 2 == 0:
                    current += int(args[1]) - 1
            case "jio":
                if registers[args[0]] == 1:
                    current += int(args[1]) - 1
        current += 1
    return registers["b"]


with open("data") as f:
    instructions = f.read().replace(",", "").splitlines()

# ==== PART 1 ====
print(exec({"a": 0, "b": 0}, instructions))

# ==== PART 2 ====
print(exec({"a": 1, "b": 0}, instructions))
