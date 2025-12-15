import re
from collections import defaultdict
from math import prod

with open("data") as f:
    instructions = f.read().splitlines()

compares_17_61 = ""

# ==== PART 1 ====
destinations = defaultdict(set)
executed = dict(zip(instructions, [False] * len(instructions)))
while not all(executed.values()):
    for instruction in instructions:
        if executed[instruction]:
            continue

        if instruction.startswith("value"):
            value, dst = re.search(r"(\d+).*(bot \d+)", instruction).groups()
            if len(destinations[dst]) < 2:
                destinations[dst].add(int(value))
                executed[instruction] = True
        else:  # starts with "bot"
            bot, low, high = re.findall(r"(bot \d+|output \d+)", instruction)
            microchips = destinations[bot]
            if len(microchips) == 2:
                if microchips == {17, 61}:
                    compares_17_61 = bot.split()[-1]
                destinations[low].add(min(destinations[bot]))
                destinations[high].add(max(destinations[bot]))
                destinations[bot] = set()
                executed[instruction] = True

print(compares_17_61)

# ==== PART 2 ====
print(prod(destinations[f"output {i}"].pop() for i in (0, 1, 2)))
