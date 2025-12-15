from math import log, floor

with open("data") as f:
    N = int(f.read())

# ==== PART 1 ====
# write any number N as 2^n + k, where n is the largest integer s.t. 2^n < N, and 0 <= k < 2^n.
# Then: f(2^n + k) = 2k + 1

print(2 * (N - 2 ** floor(log(N, 2))) + 1)

# ==== PART 2 ====
# write any number N as 3^n + k, where n is the largest integer s.t. 3^n < N, and 1 <= k < 2 * 3^n.
# Then:
#               |- k,          if 1 <= k < 3^n
# f(3^n + k) = -|
#               |- 2k - 3^n,   if 3^n <= k < 2*3^n

l = 3 ** floor(log(N, 3))
print(k if 1 <= (k := (N - l)) < l else 2 * k - l)
