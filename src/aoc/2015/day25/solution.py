import re

with open("data") as f:
    row, col = map(int, re.search(r"(\d+)\D*(\d+)", f.read()).groups())

current = 20151125
for _ in range(1, (row + col - 1) * (row + col - 2) // 2 + col):
    current = (current * 252533) % 33554393
print(current)
