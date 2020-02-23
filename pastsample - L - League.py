# https://atcoder.jp/contests/past-sample/tasks/abc139_e

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
alst = []
for _ in range(n):
    a = [int(j) - 1 for j in readline().split()]
    a.reverse()
    alst.append(a)

c = 0
ans = 0
s = set()
while True:
    if not s:
        for i in range(n):
            if alst[alst[i][-1]][-1] == i:
                s.add(i)
    else:
        p, s = s, set()
        for i in p:
            ai = alst[i]
            if ai and alst[ai[-1]] and alst[ai[-1]][-1] == i:
                s.add(i)
                s.add(ai[-1])
    if not s:
        print(-1)
        quit()
    for i in s:
        alst[i].pop()
        if not alst[i]:
            c += 1
    ans += 1
    if c == n:
        break
print(ans)
