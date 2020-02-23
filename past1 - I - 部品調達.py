# https://atcoder.jp/contests/past201912-open/tasks/past201912_i

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())
alst = []
clst = []
for _ in range(m):
    c, a = input().split()
    alst.append(int(a))
    c = c.replace('Y', '1').replace('N', '0')
    clst.append(int(c, 2))
mm = m * (10 ** 9)
cost = [mm] * (1 << n)
cost[0] = 0
for ai, ci in zip(alst, clst):
    for j in range(1 << n):
        tc = ci | j
        if cost[tc] > ai + cost[j]:
            cost[tc] = ai + cost[j]
ret = cost[-1]
print(ret if ret < mm else -1)
