from functools import lru_cache


@lru_cache
def wires(node):
    if node.isdigit():
        return int(node)

    parts = node.split()
    l, r = parts[0], parts[-1]
    if "OR" in parts:
        return wires(l) | wires(r)
    elif "AND" in parts:
        return wires(l) & wires(r)
    elif "LSHIFT" in parts:
        return wires(l) << int(r)
    elif "RSHIFT" in parts:
        return wires(l) >> int(r)
    elif "NOT" in parts:
        return ~wires(r)
    return wires(instructions[l])


def parse(instruction):
    src, dst = instruction.split(" -> ", 1)
    return dst, src


with open("data") as f:
    instructions = dict(parse(i) for i in f.read().splitlines())

# ==== PART 1 ====
a_value = wires(instructions["a"])
print(a_value)

# ==== PART 2 ====
wires.cache_clear()
instructions["b"] = str(a_value)
print(wires(instructions["a"]))
