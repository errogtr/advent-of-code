import re


with open("data") as f:
    ips = f.read().splitlines()


# ==== PART 1 ====
abba = [
    re.compile(r"(?:^|])\w*(\w)((?!\1)\w)\2\1\w*(?:\[|$)"),  # ]...abba...[
    re.compile(r"^(?!.*\[\w*(\w)((?!\1)\w)\2\1\w*])"),  # NOT [...abba...]s
]
print(sum(all(r.search(ip) for r in abba) for ip in ips))

# ==== PART 2 ====
aba = [
    re.compile(r"(?:^|])\w*(\w)((?!\1)\w)\1.*\[\w*\2\1\2"),  # ...aba...[...bab...]
    re.compile(
        r"\[\w*(\w)((?!\1)\w)\1\w*].*\2\1\2\w*(?:\[|$)"
    ),  # ...[...bab...]...aba...
]
print(sum(any(r.search(ip) for r in aba) for ip in ips))
