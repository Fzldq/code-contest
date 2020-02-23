# https://atcoder.jp/contests/past-sample/tasks/abc141_d

import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
alst = [-int(i) for i in input().split()]
heapq.heapify(alst)
for _ in range(m):
    heapq.heappushpop(alst, -(-alst[0] // 2))
print(-sum(alst))
