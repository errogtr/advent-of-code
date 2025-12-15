from hashlib import md5
import re
from functools import cache


@cache
def stretch(s, n):
    for _ in range(n+1):
        s = md5(s.encode()).hexdigest()
    return s


def index(salt, reps):
    key, i = 0, 0
    while key < 64:
        if m := re.search(r"([0-9a-f])\1\1", stretch(f"{salt}{i}", reps)):
            for j in range(1, 1001):
                if m.group() + m.group()[:2] in stretch(f"{salt}{i + j}", reps):
                    key += 1
                    break
        i += 1
    return i - 1


with open("data") as f:
    salt = f.read()

# ==== PART 1 ====
print(index(salt, reps=0))

# ==== PART 2 ====
print(index(salt, reps=2016))
