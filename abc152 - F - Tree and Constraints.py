# https://atcoder.jp/contests/abc152/tasks/abc152_f

import io
from collections import defaultdict

s = '''8
1 2
2 3
4 3
2 5
6 3
6 7
8 6
5
2 7
3 5
1 6
2 8
7 8
'''

f = io.StringIO(s)
readline = f.readline


def dfs(s, t):
    visited = 0
    q = [(s, 0)]
    while q:
        v, used = q.pop()
        if v == t:
            return used
        visited |= used
        for lb, u in graph[v]:
            if lb & visited:
                continue
            q.append((u, used | lb))


n = int(readline())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, readline().split())
    lb = 1 << i
    graph[a].append([lb, b])
    graph[b].append([lb, a])

m = int(readline())
conditions = []
for i in range(m):
    u, v = map(int, readline().split())
    conditions.append(dfs(u, v))

link_conditions = [int(''.join(b), 2) for b in zip(*map(('{:0' + str(n - 1) + 'b}').format, conditions))]

dp = defaultdict(int)
dp[0] = 1  # 所有路都是白的
for lc in link_conditions:  # O(2**N)
    # 使某条路变黑，lc为使用这条路的条件们
    for fulfilled, pattern in list(dp.items()):
        dp[fulfilled | lc] += pattern  # 使这条路变黑后，增加了几种情况
print(dp[(1 << m) - 1])
