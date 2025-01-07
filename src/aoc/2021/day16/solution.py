from itertools import batched
from math import prod
from pathlib import Path


def hex2bin(c: str) -> str:
    return bin(int(c, 16))[2:]


def parse(packet: str) -> tuple[int, int, int]:
    version, type_id = int(packet[:3], 2), packet[3:6]
    if type_id == "100":  # literal
        value, i = literal(packet)
        return version, value, i

    if packet[6] == "0":
        version, values, i = op_type_zero(packet, version)
    else:  # length_type_id == "1"
        version, values, i = op_type_one(packet, version)

    match type_id:
        case "000":
            value = sum(values)
        case "001":
            value = prod(values)
        case "010":
            value = min(values)
        case "011":
            value = max(values)
        case "101":
            value = gt(*values)
        case "110":
            value = lt(*values)
        case "111":
            value = eq(*values)

    return version, value, i


def literal(packet) -> tuple[int, int]:
    value = ""
    i = 6
    for prefix, *group in batched(packet[i:], 5):
        value += "".join(group)
        i += 5
        if prefix == "0":
            break
    return int(value, 2), i


def op_type_zero(packet: str, version: int) -> tuple[int, list[int], int]:
    i = 22
    l = int(packet[7:i], 2)
    values = list()
    while i - 22 < l:
        version_sub, value, offset = parse(packet[i:])
        version += version_sub
        i += offset
        values.append(value)
    return version, values, i


def op_type_one(packet: str, version: int) -> tuple[int, list[int], int]:
    values = list()
    i = 18
    n = int(packet[7:i], 2)
    for _ in range(n):
        version_sub, value, offset = parse(packet[i:])
        version += version_sub
        i += offset
        values.append(value)
    return version, values, i


def gt(x: int, y: int) -> bool:
    return x > y


def lt(x: int, y: int) -> bool:
    return x < y


def eq(x: int, y: int) -> bool:
    return x == y


def main(input_path: Path):
    with input_path.open() as f:
        hex_packet = f.read()

    packet = "".join(hex2bin(c).zfill(4) for c in hex_packet)
    version, value, _ = parse(packet)

    # ==== PART 1 ====
    print(version)

    # ==== PART 2 ====
    print(value)
