from hashlib import md5
from itertools import count


def hash(s):
    return md5(s.encode()).hexdigest()


def lowest(key, l):
    for i in count():
        if hash(f"{key}{i}").startswith("0" * l):
            return i


with open("data") as f:
    key = f.read()

# ==== PART 1 ====
print(lowest(key, 5))

# ==== PART 2 ====
print(lowest(key, 6))
