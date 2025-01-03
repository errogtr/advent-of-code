with open("data") as f:
    literals = f.read().splitlines()

# ==== PART 1 ====
print(sum(len(s) - len(eval(s)) for s in literals))

# ==== PART 2 ====
print(
    sum(2 + len(s.replace("\\", "\\\\").replace('"', '\\"')) - len(s) for s in literals)
)
