from pathlib import Path
import re


def generate(generator, factor, mod):
    while True:
        generator = (generator * factor) % 2147483647
        if generator % mod == 0:
            yield generator


def generate_A(generator, mod_A):
    return generate(generator, 16807, mod_A)


def generate_B(generator, mod_A):
    return generate(generator, 48271, mod_A)


def judge(n, seed_A, seed_B, mod_A, mod_B):
    gen_A, gen_B = seed_A, seed_B
    matches = 0
    for _ in range(n):
        gen_A = next(generate_A(gen_A, mod_A))
        gen_B = next(generate_B(gen_B, mod_B))
        matches += gen_A & 0xFFFF == gen_B & 0xFFFF
    return matches


def main(input_path: Path):
    with input_path.open() as f:
        seed_A, seed_B = map(int, re.findall(r"\d+", f.read()))

    # ==== PART 1 ====
    print(judge(40_000_000, seed_A, seed_B, 1, 1))
    
    # ==== PART  ====
    print(judge(5_000_000, seed_A, seed_B, 4, 8))
