# https://atcoder.jp/contests/abc151/tasks/abc151_d

import sys
from collections import deque
readline = sys.stdin.readline


H, W = map(int, readline().split())
grid = '#' * (W + 2) + \
    ''.join('#' + readline().strip() + '#' for _ in range(H)) + \
    '#' * (W + 2)
INF = 400


def shortest(grid, start, cost=0):
    dist = [INF] * (H + 2) * (W + 2)
    move = (-1, 1, W + 2, -W - 2)
    st = deque([start])
    dist[start] = 0
    while(st):
        sx = st.popleft()
        c = dist[sx]
        for a in move:
            x = sx + a
            if grid[x] == '#':
                continue
            dx = c + 1
            if dist[x] <= dx:
                continue
            dist[x] = dx
            st.append(x)
    return max(x for x in dist if x < INF)


m = 0
for i in range(W + 3, (H + 1) * (W + 2) - 1):
    if grid[i] == '#':
        continue
    tm = shortest(grid, i)
    if m < tm:
        m = tm
print(m)
