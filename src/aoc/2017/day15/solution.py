from pathlib import Path
import re

from tqdm import tqdm


def judge(n, seed_A, seed_B, mod_A, mod_B):
    gen_A, gen_B = seed_A, seed_B
    matches = 0
    for _ in tqdm(range(n)):
        while True:
            gen_A = (gen_A * 16807) % 2147483647
            if gen_A % mod_A == 0:
                break

        while True:
            gen_B = (gen_B * 48271) % 2147483647
            if gen_B % mod_B == 0:
                break

        if gen_A & 0xFFFF == gen_B & 0xFFFF:
            matches += 1
    return matches


def main(input_path: Path):
    with input_path.open() as f:
        seed_A, seed_B = map(int, re.findall(r"\d+", f.read()))

    # ==== PART 1 ====
    print(judge(40_000_000, seed_A, seed_B, 1, 1))

    # ==== PART  ====
    print(judge(5_000_000, seed_A, seed_B, 4, 8))
