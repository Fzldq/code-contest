# https://atcoder.jp/contests/past201912-open/tasks/past201912_g

from itertools import combinations

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
r = readlines()
lst = []
for i in r:
    lst.append([int(j) for j in i.strip().split()])
res = - 10e9
for i in range(3 ** n):
    tg = []
    ti = i
    h = 0
    group = [[] for _ in range(3)]
    for j in range(n):
        tg.append(ti % 3)
        ti //= 3
    for idx, tg1 in enumerate(tg):
        group[tg1].append(idx)
    for group1 in group:
        if len(group1) < 2:
            continue
        for (a, b) in combinations(group1, 2):
            if a < b:
                h += lst[a][b - a - 1]
            else:
                h += lst[b][a - b - 1]
    if res < h:
        res = h
print(res)
