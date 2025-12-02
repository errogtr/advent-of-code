from math import ceil
from pathlib import Path


def main(input_path: Path):
    with input_path.open() as f:
        data = f.read()

    max_len = 0  # max digits number
    id_ranges = list()  # list of int ranges [(lower bound, upper bound)]
    for id_range in data.split(","):
        low, up = id_range.split("-")
        max_len = max(max_len, len(up))
        id_ranges.append((int(low), int(up)))

    invalid = set()
    for k in range(2, max_len + 1):
        for n in range(10 ** ceil(max_len / k)):
            
            rep = int(str(n) * k)
            for l, r in id_ranges:
                if l <= rep <= r:
                    invalid.add(rep)

    print(sum(invalid))


    # for l, r in id_ranges:
    #     ll = len(l)
    #     lr = len(r)

    #     # both l, r have odd digits number
    #     if ll % 2 and lr % 2:
    #         continue

    #     # l has odd digit number and r has even digit number
    #     if ll % 2 and lr % 2 == 0:
    #         start = 10 ** ll
    #         end = int(r)
        
    #     # l has even digit number and r has odd digit number
    #     elif ll % 2 == 0 and lr % 2:
    #         start = int(l)
    #         end = 10 ** (lr - 1) - 1

    #     # both l, r have even digits number
    #     else:
    #         start, end = int(l), int(r)

    #     for n in range(start, end + 1):




        

        

