with open("data") as f:
    data = f.read().splitlines()

horizontal, depth, aim = 0, 0, 0
for line in data:
    direction, steps = line.split()
    match direction:
        case "forward":
            horizontal += int(steps)
            depth += aim * int(steps)
        case "down":
            aim += int(steps)
        case "up":
            aim -= int(steps)

# ==== PART 1 ====
print(horizontal * aim)

# ==== PART 2 ====
print(horizontal * depth)
