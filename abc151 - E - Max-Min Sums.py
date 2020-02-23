# https://atcoder.jp/contests/abc151/tasks/abc151_e

import sys
read = sys.stdin.read

n, k, *alst = map(int, read().split())
alst.sort()
lst1 = alst[k - 1:]
lst2 = alst[n - k::-1]
mod = 10 ** 9 + 7
res = 0
prep = 1
for i in range(n - k + 1):
    res += prep * (lst1[i] - lst2[i])
    res %= mod
    prep = prep * (i + k) * pow(i + 1, mod - 2, mod)
    prep %= mod

print(res)
