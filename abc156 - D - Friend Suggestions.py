# https://atcoder.jp/contests/abc157/tasks/abc157_d

import io

s = '''10 9 3
10 1
6 7
8 2
2 5
8 4
7 3
10 9
6 4
5 8
2 6
7 5
3 1
'''

f = io.StringIO(s)
readline = f.readline

N, M, K = map(int, readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, readline().split())
    graph[a].append(b)
    graph[b].append(a)

block = [[] for _ in range(N + 1)]
for _ in range(K):
    c, d = map(int, readline().split())
    block[c].append(d)
    block[d].append(c)


def dfs(v):
    gs = 1
    stack = [v]
    visited[v] = group
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if not visited[y]:
                visited[y] = group
                gs += 1
                stack.append(y)
    return gs


visited = [False] * (N + 1)
group_size = {}
group = 1
for i in range(1, N + 1):
    if not visited[i]:
        group_size[group] = dfs(i)
        group += 1

res = []
for i in range(1, N + 1):
    tmp = group_size[visited[i]] - len(graph[i]) - 1
    for j in block[i]:
        if visited[i] == visited[j]:
            tmp -= 1
    res += [tmp]
print(res)
