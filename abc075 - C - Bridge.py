# https://atcoder.jp/contests/abc075/tasks/abc075_c

import io

s = '''7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7
'''

readline = io.StringIO(s).readline
N, M = map(int, readline().split())
graph = [[False for i in range(N)] for i in range(N)]
ab = []
for i in range(M):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    ab.append([a, b])
    graph[a][b] = graph[b][a] = True

all_use = (1 << N) - 1


def rec(v, use):
    use |= 1 << v
    for u in range(N):
        if (not graph[u][v]) or (use >> u) & 1:
            continue
        use |= rec(u, use)
    return use


ans = 0
for a, b in ab:
    graph[a][b] = graph[b][a] = False
    if rec(0, 0) != all_use:
        ans += 1
    graph[a][b] = graph[b][a] = True
print(ans)
