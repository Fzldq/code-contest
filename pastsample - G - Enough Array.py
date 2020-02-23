# https://atcoder.jp/contests/past-sample/tasks/abc130_d

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
alst = [int(i) for i in input().split()]
s = 0
end = 0
c = 0
over = False
for i in range(n):
    while s < k:
        if end == n:
            over = True
            break
        s += alst[end]
        end += 1
    if over:
        break
    c += n - end + 1
    s -= alst[i]
print(c)
