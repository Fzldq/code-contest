import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n, u, v = map(int, readline().split())
m = map(int, read().split())
data = list(zip(m, m))

graph = [[] for _ in range(n + 1)]
for a, b in data:
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    dist = [None] * (n + 1)
    dist[v] = 0
    stack = [v]
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist[y] is None:
                dist[y] = dist[x] + 1
                stack.append(y)
    return dist
