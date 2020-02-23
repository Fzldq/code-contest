# https://atcoder.jp/contests/abc153/tasks/abc153_e

import numpy as np
import sys
read = sys.stdin.read

h, n, *ab = map(int, read().split())
a = np.array(ab[::2])
b = np.array(ab[1::2])

magic = np.zeros(h + 1, dtype=np.int64)
for i in range(1, 1 + h):
    magic[i] = np.min(magic[np.maximum(i - a, 0)] + b)
print(magic[h])


# another method

import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

H, N = map(int, input().split())

AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))


@lru_cache(maxsize=None)
def f(h):
    if h <= 0:
        return 0
    best = float("inf")
    for a, b in AB:
        val = b + f(h - a)
        if val < best:
            best = val
        else:
            break
    return best


AB.sort(key=lambda ab: (ab[0] / ab[1], -ab[0]), reverse=True)
bestA, bestB = AB[0]

print(f(H))
