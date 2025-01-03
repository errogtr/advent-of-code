import re

with open("data") as f:
    replacements, medicine = f.read().split("\n\n")
    replacements = [r.split(" => ") for r in replacements.splitlines()]

# ==== PART 1 ====
molecules = set()
for source, replacement in replacements:
    for sub in re.finditer(source, medicine):
        molecules.add(medicine[:sub.start()] + replacement + medicine[sub.end():])
print(len(molecules))

# ==== PART 2 ====
# this works because every replacement is 'unique': a replacement X is never contained in a replacement Y
count = 0
while medicine != "e":
    for src, replacement in replacements:
        if replacement in medicine:
            medicine, n = re.subn(replacement, src, medicine)
            count += n
print(count)
