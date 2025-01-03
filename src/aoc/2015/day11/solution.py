import re


def from_base_26(password):
    return sum((ord(c) - 97) * 26**i for i, c in enumerate(reversed(password)))


def to_base_26(num):
    password = ""
    while num:
        password += chr(num % 26 + 97)
        num //= 26
    return password[::-1]


def validate(password):
    return all(
        (
            re.search(
                r"abc|bcd|cde|def|efg|fgh|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", password
            ),
            re.search(r"[iol]", password) is None,
            re.search(r"(\w)\1.*(\w)\2", password),
        )
    )


def increment(password):
    return to_base_26(from_base_26(password) + 1)


def next_password(password):
    while not validate(password):
        password = increment(password)
    return password


with open("data") as f:
    password = f.read()


# ==== PART 1 ====
password = next_password(password)
print(password)

# ==== PART 2 ====
print(next_password(increment(password)))
