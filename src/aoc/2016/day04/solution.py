from collections import Counter
from itertools import groupby
from operator import itemgetter
import re

with open("data") as f:
    rooms = f.read().splitlines()

# ==== PART 1 ====
real = list()
for room in rooms:
    encrypted, sector, checksum = re.match(r"(.+)-(\d+)\[(\w+)]", room).groups()
    counts = Counter(encrypted.replace("-", "")).most_common()
    ordered = "".join(
        "".join(c for c, _ in sorted(g)) for _, g in groupby(counts, key=itemgetter(1))
    )
    if ordered[:5] == checksum:
        real.append((encrypted, int(sector)))
print(sum(s for _, s in real))

# ==== PART 2 ====
northpole_id = None
for name, sector in real:
    decrypted = "".join(
        chr((ord(c) - 97 + sector) % 26 + 97) for c in name if c.isalpha()
    )
    if decrypted.startswith("northpole"):
        northpole_id = sector
        break
print(northpole_id)
