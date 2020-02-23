# https://atcoder.jp/contests/past-sample/tasks/abc138_e

import sys
import bisect
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S, T = input(), input()
n = len(S)
D = {chr(i + ord("a")): [] for i in range(26)}
for i, s in enumerate(S):
    D[s].append(i)
for t in set(T):
    if not D[t]:
        print(-1)
        quit()
p = 0
res = 0
for t in T:
    i = bisect.bisect_left(D[t], p)
    if i == len(D[t]):
        res += n
        p = D[t][0] + 1
    else:
        p = D[t][i] + 1
res += p
print(res)
