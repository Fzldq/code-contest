# https://atcoder.jp/contests/past201912-open/tasks/past201912_j

import io
from heapq import heappop, heappush

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


input_data = '''10 10
1 2 265 1544 0 1548 4334 9846 58 0
21 0 50 44 2 388 5 0 0 4
170 0 2 1 54 1379 50 3 41 0
310 0 1 0 2163 0 226 26 3 12
151 33 0 9 0 0 0 36 365 2286
0 3 12 3 9 317 645 100 21 4
52 1 569 0 144 0 6 202 25 0
8869 19 2058 1948 1252 1002 7 1750 0 5
0 3 8 29 2 4403 0 0 0 5
0 17 93 9367 159 6 1 216 0 0
'''


def shortest(grid, start, cost=0):
    dist = [[INF for _ in range(COL)] for _ in range(ROW)]
    # path = [[[] for _ in range(COL)] for _ in range(ROW)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    st = [(cost, start)]
    dist[start[0]][start[1]] = grid[start[0]][start[1]] + cost
    # path[start[0]][start[1]] = start
    while(st):
        c, [sx, sy] = heappop(st)
        for a, b in zip(dx, dy):
            x = sx + a
            y = sy + b
            dxy = dist[sx][sy] + grid[x][y]
            if dist[x][y] <= dxy:
                continue
            dist[x][y] = dxy
            # path[x][y] = path[sx][sy][:]
            # path[x][y].append([x, y])
            heappush(st, (dist[x][y], [x, y]))
    return dist


f = io.StringIO(input_data)

ROW, COL = map(int, f.readline().split())
ROW += 2
COL += 2
INF = 10e9
grid = [[INF] * COL]

for _ in range(ROW - 2):
    grid.append([INF] + list(map(int, f.readline().split())) + [INF])
grid += [[INF] * COL]
LD = [ROW - 2, 1]
RU = [1, COL - 2]
RD = [ROW - 2, COL - 2]

dis1 = shortest(grid, LD)
dis2 = shortest(grid, RU)
dis3 = shortest(grid, RD)
res = 10e9
for i in range(1, ROW - 1):
    for j in range(1, COL - 1):
        d = dis1[i][j] + dis2[i][j] + dis3[i][j] - 2 * grid[i][j]
        if res > d:
            res = d
print(res)
