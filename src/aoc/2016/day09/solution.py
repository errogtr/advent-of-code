import re


def decompress(section, once=True):
    i, length = 0, 0
    while i < len(section):
        subsection = section[i:]
        if m := re.match(r"\((\d+)x(\d+)\)", subsection):
            chars, reps = map(int, m.groups())
            start, end = m.end(), m.end() + chars
            if once:
                length += chars * reps
            else:
                length += decompress(subsection[start:end], once) * reps
            i += end
        else:
            length += 1
            i += 1
    return length


with open("data") as f:
    section = f.read()

# ==== PART 1 ====
print(decompress(section))

# ==== PART 2 ====
print(decompress(section, once=False))
