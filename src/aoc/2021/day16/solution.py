from itertools import batched
from math import prod
from pathlib import Path


OpsMap = dict[str, callable]


def hex2bin(c: str) -> str:
    return bin(int(c, 16))[2:]


def parse(packet: str, ops: OpsMap) -> int:
    version, type_id = int(packet[:3], 2), packet[3:6]
    if type_id == "100":  # literal
        value = ""
        i = 6
        for prefix, *group in batched(packet[i:], 5):
            value += "".join(group)
            i += 5
            if prefix == "0":
                break
        return i, version, int(value, 2)
    
    values = list()
    length_type_id = packet[6]
    if length_type_id == "0":
        i = 22
        l = int(packet[7:i], 2)
        while i - 22 < l:
            offset, version_sub, value = parse(packet[i:], ops)
            version += version_sub
            i += offset
            values.append(value)
    else:  # length_type_id == "1"
        i = 18
        n = int(packet[7:i], 2)
        for _ in range(n):
            offset, version_sub, value = parse(packet[i:], ops)
            version += version_sub
            i += offset
            values.append(value)
    return i, version, ops[type_id](values)


def gt(values) -> bool:
    x, y, *_ = values
    return x > y

def lt(values) -> bool:
    x, y, *_ = values
    return x < y

def eq(values) -> bool:
    x, y, *_ = values
    return x == y


def main(input_path: Path):
    ops = {
        "000": sum,
        "001": prod,
        "010": min,
        "011": max,
        "101": gt,
        "110": lt,
        "111": eq,
    }
    with input_path.open() as f:
        hex_packet = f.read()

    packet = "".join(hex2bin(c).zfill(4) for c in hex_packet)
    _, version, value = parse(packet, ops)

    # ==== PART 1 ====
    print(version)    

    # ==== PART 2 ====
    print(value) 
